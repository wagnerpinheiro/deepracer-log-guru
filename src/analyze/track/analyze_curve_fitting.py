#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

import tkinter as tk

import src.utils.geometry as geometry
from src.analyze.core.controls import CurveDirectionControl, CurveSteeringDegreesControl,\
    CurveSpeedControl, CurveInitialSlideControl

from src.analyze.track.track_analyzer import TrackAnalyzer
from src.episode.episode import extract_all_sequences
from src.graphics.track_graphics import TrackGraphics
from src.sequences.sequences import Sequences

BACKWARDS_DISTANCE = 2


class AnalyzeCurveFitting(TrackAnalyzer):

    def __init__(self, guru_parent_redraw, track_graphics: TrackGraphics, control_frame: tk.Frame):
        super().__init__(guru_parent_redraw, track_graphics, control_frame)

        self._curve_direction_control = CurveDirectionControl(guru_parent_redraw, control_frame)
        self._curve_steering_degrees_control = CurveSteeringDegreesControl(guru_parent_redraw, control_frame)
        self._entry_speed_control = CurveSpeedControl(guru_parent_redraw, control_frame, "Entry")
        self._action_speed_control = CurveSpeedControl(guru_parent_redraw, control_frame, "Action")
        self._initial_slide_control = CurveInitialSlideControl(guru_parent_redraw, control_frame)

        self._all_sequences = Sequences()
        self._episode_sequences = Sequences()

        self._chosen_point = None
        self._chosen_bearing = None
        self._backwards_point = None

        self._all_sequences.load()

    def build_control_frame(self, control_frame):
        self._curve_direction_control.add_to_control_frame()
        self._curve_steering_degrees_control.add_to_control_frame()
        self._action_speed_control.add_to_control_frame()
        self._entry_speed_control.add_to_control_frame()
        self._initial_slide_control.add_to_control_frame()

    def redraw(self):
        if self._chosen_point and self._chosen_bearing:
            self.track_graphics.plot_angle_line(self._chosen_point, self._chosen_bearing - 180, BACKWARDS_DISTANCE, 2, "green")

            action_steering_angle_match = self._curve_steering_degrees_control.get_steering_range()
            if self._curve_direction_control.direction_right():
                (s1, s2) = action_steering_angle_match
                action_steering_angle_match = (-s1, -s2)

            initial_track_speed_match = self._entry_speed_control.get_speed_range()
            initial_slide_match = self._initial_slide_control.get_initial_slide_range()
            action_speed_match = self._action_speed_control.get_speed_range()

            sequences = self._all_sequences.get_matches(initial_track_speed_match, initial_slide_match, action_speed_match, action_steering_angle_match)

            for s in sequences:
                points = s.get_plot_points(self._chosen_point, self._chosen_bearing)
                seconds = 0.0
                for p in points:
                    if seconds < 1:
                        colour = "green"
                    elif seconds < 2:
                        colour = "yellow"
                    else:
                        colour = "pink"
                    self.track_graphics.plot_dot(p, 2, colour)
                    seconds += 1/15

    def right_button_pressed(self, chosen_point):
        chose_backwards_point = False
        if self._backwards_point:
            backwards_distance = geometry.get_distance_between_points(chosen_point, self._backwards_point)
            primary_distance = geometry.get_distance_between_points(chosen_point, self._chosen_point)
            chose_backwards_point = backwards_distance < 0.5 * primary_distance and abs(primary_distance - BACKWARDS_DISTANCE) < 0.25 * BACKWARDS_DISTANCE

        if chose_backwards_point:
            self._backwards_point = chosen_point
            self._chosen_bearing = geometry.get_bearing_between_points(self._backwards_point, self._chosen_point)
        else:
            self._chosen_point, waypoint_id = self.current_track.get_adjusted_point_on_track(chosen_point)
            self._chosen_bearing = self.current_track.get_bearing_at_waypoint(waypoint_id)
            self._backwards_point = geometry.get_point_at_bearing(self._chosen_point, self._chosen_bearing - 180, BACKWARDS_DISTANCE)

        self.guru_parent_redraw()

    def warning_track_changed(self):
        self._chosen_point = None
        self._backwards_point = None

    def warning_all_episodes_changed(self):
        self._episode_sequences = extract_all_sequences(self.all_episodes, 10)
        self._all_sequences.add_sequences(self._episode_sequences)
        self._all_sequences.save()
        self.guru_parent_redraw()

