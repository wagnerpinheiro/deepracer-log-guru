#
# DeepRacer Guru
#
# Version 3.0 onwards
#
# Copyright (c) 2021 dmh23
#

from src.tracks.track import Track
import src.personalize.configuration.personal_track_annotations as config


class JochemTurnpikeTrack(Track):
    def __init__(self):
        super().__init__()

        self._ui_name = "Jochem Turnpike"
        self._ui_description = "Put your developer skills to the test on the Jochem Turnpike named after AWS Machine learning Community member and re:Invent 2021 finalist, Jochem Lugtenburg. This track features no shortage of zigzags and tricky hairpin turns. Does your model have what it takes to make it around the broad, sweeping turns and climb the leaderboard? Get racing today and find out!"
        self._ui_length_in_m = 99.99  # metres     (NOT STATED)
        self._ui_width_in_cm = 107  # centimetres
        self._world_name = "2022_august_open"
        self._track_sector_dividers = [29, 64, 83, 110]
        self._annotations = config.jochem_turnpike_annotations
        self._track_width = 1.067

        self._track_waypoints = [(-7.152451515197754, 1.001694679260254), (-7.1784443855285645, 0.7017773985862732),
                                 (-7.191962480545044, 0.40103815495967865), (-7.1970014572143555, 0.10003244131803157),
                                 (-7.19492244720459, -0.2009738981723821), (-7.187003135681152, -0.501918151974678),
                                 (-7.180588960647583, -0.8028974533081035), (-7.172152042388916, -1.1038255095481873),
                                 (-7.158402442932129, -1.404554009437557), (-7.1360924243927, -1.70476496219635),
                                 (-7.105409860610962, -2.004241466522217), (-7.059787511825562, -2.301728963851924),
                                 (-6.981626510620117, -2.592269539833069), (-6.857151985168455, -2.865949511528018),
                                 (-6.674427032470703, -3.10434353351593), (-6.4372398853302, -3.28915798664093),
                                 (-6.184372425079346, -3.4523099660873413), (-5.918492078781128, -3.5934101343154907),
                                 (-5.642937421798706, -3.7145450115203857), (-5.360129117965698, -3.8176634311676025),
                                 (-5.072028875350952, -3.904926061630249), (-4.780129432678223, -3.978447914123535),
                                 (-4.485681056976318, -4.041495084762573), (-4.184867858886719, -4.047769904136658),
                                 (-3.885171055793762, -4.020549058914185), (-3.5888564586639404, -3.967507004737854),
                                 (-3.296796441078186, -3.8945831060409546), (-3.009177565574646, -3.8057055473327637),
                                 (-2.725923538208008, -3.7037534713745117), (-2.446863532066345, -3.590833067893982),
                                 (-2.1718364357948303, -3.468423008918762), (-1.9003545045852661, -3.338273525238037),
                                 (-1.6365500092506409, -3.193374991416931), (-1.3853605389595032, -3.027525544166565),
                                 (-1.183251827955246, -2.805064558982849), (-0.9599289298057556, -2.6058086156845093),
                                 (-0.6777525842189789, -2.503422498703003), (-0.38381171226501465, -2.438413977622986),
                                 (-0.10530319809913635, -2.326894521713257), (0.11551439762115479, -2.1235689520835876),
                                 (0.33583291131071746, -1.9185495376586914), (0.5760912001132965, -1.7373639345169067),
                                 (0.8359667658805847, -1.5857210159301758), (1.1134151816368103, -1.4693804383277893),
                                 (1.4031519889831543, -1.3879605829715729), (1.699357509613037, -1.3347405195236206),
                                 (1.9989050030708313, -1.3052586913108826), (2.288704991340637, -1.2434021830558777),
                                 (2.5446665287017822, -1.0850750803947449), (2.7965439558029175, -0.9202039837837219),
                                 (3.0630104541778564, -0.7807751148939133), (3.310854434967041, -0.6101177111268044),
                                 (3.5530980825424194, -0.43143417313694954), (3.820249557495117, -0.2943778410553932),
                                 (4.117615461349487, -0.2649547606706619), (4.117615461349487, -0.2649547606706619),
                                 (4.4046924114227295, -0.3559295982122421), (4.69898796081543, -0.4194209426641464),
                                 (4.9984846115112305, -0.450405266135931), (5.2994585037231445, -0.4430101364850998),
                                 (5.596153020858765, -0.39203836396336555), (5.8808794021606445, -0.29435595870018005),
                                 (6.145330429077148, -0.15058104693889618), (6.3827064037323, 0.03453025221824646),
                                 (6.5893394947052, 0.2534659132361412), (6.7647926807403564, 0.4981161504983899),
                                 (6.9109954833984375, 0.7613103091716766), (7.030421018600464, 1.037620097398758),
                                 (7.127272367477417, 1.3227970004081726), (7.195359230041504, 1.615845501422882),
                                 (7.234156847000122, 1.9143420457839966), (7.251775503158569, 2.214840531349182),
                                 (7.249213457107544, 2.5158544778823853), (7.223695993423462, 2.8157711029052734),
                                 (7.1676695346832275, 3.1114540100097656), (7.062946081161499, 3.3931844234466553),
                                 (6.878399372100829, 3.630077958106995), (6.63496470451355, 3.8078274726867676),
                                 (6.360635995864868, 3.9314639568328857), (6.069420099258422, 4.00835645198822),
                                 (5.77101993560791, 4.049026012420654), (5.470163822174071, 4.06195855140686),
                                 (5.169196128845215, 4.05349862575531), (4.869206428527832, 4.028184175491333),
                                 (4.57068395614624, 3.989193558692932), (4.273848056793213, 3.938896059989929),
                                 (3.978752851486206, 3.8792755603790283), (3.685330033302307, 3.8119269609451294),
                                 (3.393546462059021, 3.737861394882202), (3.1027638912200928, 3.659803867340088),
                                 (2.814605951309204, 3.572806477546692), (2.52794349193573, 3.4808534383773804),
                                 (2.2421690225601196, 3.3861894607543945), (1.958292961120604, 3.285985469818115),
                                 (1.6775315403938293, 3.177370548248291), (1.4014475345611572, 3.0573480129241943),
                                 (1.1313577890396118, 2.9239054918289185), (0.8946400880813599, 2.7402859926223755),
                                 (0.6956964135169983, 2.5145745277404785), (0.5176730267703533, 2.2718464732170105),
                                 (0.3446405865252007, 2.0254999399185167), (0.1578773409128189, 1.7895684838294983),
                                 (-0.015438154339790344, 1.5435664653778076),
                                 (-0.16977708041667938, 1.2851099967956543), (-0.32548016309738037, 1.0274873375892661),
                                 (-0.5051136128604412, 0.7861504256725311), (-0.7223930209875099, 0.5783550068736084),
                                 (-0.9672155380249023, 0.40326098166406155), (-1.2250419855117798, 0.24791793525218964),
                                 (-1.487962007522583, 0.10128220915794373), (-1.7464795112609863, -0.05274839699268341),
                                 (-1.993106484413147, -0.22537130862474442), (-2.243585526943207, -0.3922645337879658),
                                 (-2.512253522872925, -0.5273129194974899), (-2.8037145137786865, -0.6028971523046494),
                                 (-3.104068398475647, -0.5914968885481358), (-3.382584571838379, -0.47886368818581104),
                                 (-3.611448884010315, -0.2835899516940117), (-3.7845566272735596, -0.03755010664463043),
                                 (-3.906159520149231, 0.23764296621084213), (-3.977962851524353, 0.5298609435558319),
                                 (-3.9911484718322754, 0.8302824795246124), (-3.9000219106674194, 1.1142942607402802),
                                 (-3.6874749660491943, 1.3267495334148407), (-3.5144025087356567, 1.5726954936981201),
                                 (-3.3944499492645264, 1.84837806224823), (-3.3363884687423706, 2.143296480178833),
                                 (-3.3467389345169067, 2.443671464920044), (-3.425958514213562, 2.7336835861206055),
                                 (-3.5932849645614624, 2.9760814905166626), (-3.885738492012024, 3.0377384424209595),
                                 (-4.183387994766235, 3.0764695405960083), (-4.480346441268921, 3.1251834630966187),
                                 (-4.780730485916138, 3.143426537513733), (-5.081469297409061, 3.1322793960571285),
                                 (-5.379847049713132, 3.09296202659607), (-5.673212528228758, 3.0258539915084843),
                                 (-5.958626508712772, 2.93044340610504), (-6.233084201812744, 2.8069945573806763),
                                 (-6.488256454467773, 2.6498680114746094), (-6.67578601837158, 2.412276506423952),
                                 (-6.832958459854124, 2.1560490131378205), (-6.954755544662475, 1.8807710409164446),
                                 (-7.045438528060913, 1.5937665104866028), (-7.109683990478516, 1.2996820211410522),
                                 (-7.152451515197754, 1.001694679260254)]
