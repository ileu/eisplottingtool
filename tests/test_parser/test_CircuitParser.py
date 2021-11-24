import numpy as np
import pytest
from numpy.testing import assert_array_almost_equal

from eisplottingtool.parser import parse_circuit

param_values = {
    'R': 1,
    'C': 1,
    'CPE_Q': 1,
    'CPE_n': 0.5,
    'W': 1,
    'Ws_R': 1,
    'Ws_T': 1,
    'Wo_R': 1,
    'Wo_T': 1,
    }

freq = np.array(
        [1000000000.0, 568986602.901831, 323745754.281766, 184206996.932673,
         104811313.415469, 59636233.1659468, 33932217.7189535, 19306977.2888326,
         10985411.4198756, 6250551.925274, 3556480.30622314, 2023589.64772516,
         1151395.39932645, 655128.556859552, 372759.372031494, 212095.088792019,
         120679.264063932, 68664.8845004299, 39069.3993705461, 22229.9648252619,
         12648.5521685529, 7196.8567300115, 4094.91506238042, 2329.95181051537,
         1325.71136559011, 754.312006335461, 429.193426012878, 244.205309454865,
         138.949549437314, 79.060432109077, 44.9843266896944, 25.5954792269953,
         14.5634847750124, 8.28642772854684, 4.71486636345739, 2.68269579527972,
         1.52641796717523, 0.868511373751352, 0.494171336132383,
         0.281176869797423, 0.159985871960606, 0.0910298177991521,
         0.051794746792312, 0.0294705170255181, 0.0167683293681101,
         0.00954095476349993, 0.00542867543932386, 0.00308884359647748,
         0.00175751062485479, 0.001]
        )
reandles_res = [(1 - 1.59154943091895e-10j), (1 - 2.79716503482165e-10j),
                (1 - 4.91604726817137e-10j), (1 - 8.64000530609954e-10j),
                (1 - 1.51849011242717e-09j), (1 - 2.6687625063277e-09j),
                (1 - 4.69037846008504e-09j), (1 - 8.24338997818952e-09j),
                (1 - 1.44878454714896e-08j), (1 - 2.54625423473974e-08j),
                (1 - 4.47506887113659e-08j),
                (1.00000000000001 - 7.86498108797947e-08j),
                (1.00000000000002 - 1.38227878264057e-07j),
                (1.00000000000006 - 2.42936964700206e-07j),
                (1.00000000000018 - 4.26964296630533e-07j),
                (1.00000000000056 - 7.5039428776153e-07j),
                (1.00000000000174 - 1.31882593356968e-06j),
                (1.00000000000537 - 2.31785059057434e-06j),
                (1.00000000001659 - 4.07364703971464e-06j),
                (1.00000000005126 - 7.15947795395859e-06j),
                (1.00000000015833 - 1.25828585711486e-05j),
                (1.00000000048905 - 2.21145076225251e-05j),
                (1.0000000015106 - 3.8866482070316e-05j),
                (1.00000000466602 - 6.83082549737678e-05j),
                (1.0000000144126 - 0.000120052482711585j),
                (1.00000004451826 - 0.000210993507553708j),
                (1.00000013750994 - 0.000370823296817538j),
                (1.00000042474656 - 0.000651725696900933j),
                (1.00000131197454 - 0.00114541382054976j),
                (1.00000405247306 - 0.00201307144263008j),
                (1.00001251734949 - 0.00353796450020693j),
                (1.0000386631239 - 0.00621784762274577j),
                (1.00011941469859 - 0.0109270507787653j),
                (1.00036876134375 - 0.0191996187154482j),
                (1.00113816940071 - 0.0337175617612039j),
                (1.00350728883365 - 0.0591184214834285j),
                (1.01075467598615 - 0.103145590941064j),
                (1.03248963766796 - 0.177296534405386j),
                (1.09397755029893 - 0.291797481721045j),
                (1.2426489056175 - 0.428684515955647j),
                (1.49739637427516 - 0.499993221087131j),
                (1.75350281551825 - 0.430971370887114j),
                (1.90423387036101 - 0.294270246632169j),
                (1.9668492017852 - 0.179030228711573j),
                (1.98902144862154 - 0.104201836778865j),
                (1.99641915536696 - 0.05973292379208j),
                (1.99883790266327 - 0.034069735345405j),
                (1.99962348002419 - 0.0194004692859489j),
                (1.99987807221078 - 0.0110414185153842j),
                (1.99996052314088 - 0.00628293726675839j)]
randles_cpe_res = [(1.00000892062058 - 8.92046142724053e-06j),
                   (1.00001182616809 - 1.18258883788401e-05j),
                   (1.00001567808544 - 1.56775938539714e-05j),
                   (1.00002078461606 - 2.07837520904987e-05j),
                   (1.00002755440172 - 2.75528833092262e-05j),
                   (1.00003652918348 - 3.6526514916932e-05j),
                   (1.00004842715362 - 4.84224636990012e-05j),
                   (1.00006420042773 - 6.41921854018005e-05j),
                   (1.00008511123619 - 8.50967508110213e-05j),
                   (1.00011283293192 - 0.000112807475122324j),
                   (1.00014958389737 - 0.000149539160071461j),
                   (1.00019830506614 - 0.000198226447515664j),
                   (1.00026289526438 - 0.000262757109164779j),
                   (1.00034852320349 - 0.000348280435807445j),
                   (1.00046204108712 - 0.000461614517189369j),
                   (1.00061253292277 - 0.000611783447203753j),
                   (1.00081204139692 - 0.000810724711129982j),
                   (1.0010765314368 - 0.00107421857132859j),
                   (1.00142716746481 - 0.00142310542877996j),
                   (1.00189200631944 - 0.00188487388198023j),
                   (1.00250824076825 - 0.00249572087381537j),
                   (1.00332517187709 - 0.00330320395272228j),
                   (1.00440814515977 - 0.00436961983849216j),
                   (1.0058437587222 - 0.00577624420903761j),
                   (1.00774674461038 - 0.00762853796680877j),
                   (1.01026903840845 - 0.010062334679411j),
                   (1.0136116818195 - 0.0132508197144433j),
                   (1.01804032779693 - 0.0174117068349981j),
                   (1.02390518064584 - 0.0228132773602136j),
                   (1.03166606859146 - 0.0297766781309065j),
                   (1.04192271965512 - 0.038669848081212j),
                   (1.05544860972478 - 0.0498854984488797j),
                   (1.07322293684808 - 0.0637919282567139j),
                   (1.09644781212437 - 0.0806424301244203j),
                   (1.12652519787447 - 0.10043032249987j),
                   (1.16495146798862 - 0.122689715024282j),
                   (1.21307566486261 - 0.146277359889675j),
                   (1.27168455001045 - 0.169232437420713j),
                   (1.34045872710921 - 0.188873415254491j),
                   (1.41749696467935 - 0.202277188268905j),
                   (1.49923740944068 - 0.207106369972467j),
                   (1.5810227792264 - 0.202449506545794j),
                   (1.65818479951715 - 0.189186164400969j),
                   (1.72713418022154 - 0.169634276433853j),
                   (1.78593797907923 - 0.146714366718482j),
                   (1.83425121861222 - 0.123118064941343j),
                   (1.87284536000222 - 0.100821385708608j),
                   (1.90306336178452 - 0.0809818640774946j),
                   (1.92640157028765 - 0.0640759708197357j),
                   (1.94426498173332 - 0.0501169203046683j)]
cpe_res = [(8.92062058076386e-06 - 8.92062058076386e-06j),
           (1.18261680920356e-05 - 1.18261680920356e-05j),
           (1.56780854509908e-05 - 1.56780854509908e-05j),
           (2.07846160730714e-05 - 2.07846160730714e-05j),
           (2.75544017574976e-05 - 2.75544017574976e-05j),
           (3.65291835819506e-05 - 3.65291835819506e-05j),
           (4.84271538503196e-05 - 4.84271538503196e-05j),
           (6.42004282625495e-05 - 6.42004282625495e-05j),
           (8.51112374234143e-05 - 8.51112374234143e-05j),
           (0.000112832934791658 - 0.000112832934791658j),
           (0.00014958390406619 - 0.00014958390406619j),
           (0.000198305081729888 - 0.000198305081729888j),
           (0.000262895300703588 - 0.000262895300703588j),
           (0.000348523288102976 - 0.000348523288102976j),
           (0.000462041284210952 - 0.000462041284210952j),
           (0.000612533381850309 - 0.000612533381850309j),
           (0.000812042466122301 - 0.000812042466122301j),
           (0.00107653392668015 - 0.00107653392668015j),
           (0.00142717326204323 - 0.00142717326204323j),
           (0.00189201981415702 - 0.00189201981415702j),
           (0.00250827217154965 - 0.00250827217154965j),
           (0.00332524492581676 - 0.00332524492581676j),
           (0.00440831499152612 - 0.00440831499152612j),
           (0.00584415328736744 - 0.00584415328736744j),
           (0.00774766043531381 - 0.00774766043531381j),
           (0.0102711614958283 - 0.0102711614958283j),
           (0.0136165955328311 - 0.0136165955328311j),
           (0.0180516754585177 - 0.0180516754585177j),
           (0.023931311323301 - 0.023931311323301j),
           (0.0317260114147754 - 0.0317260114147754j),
           (0.0420595339174093 - 0.0420595339174093j),
           (0.0557588021457322 - 0.0557588021457322j),
           (0.0739200777362873 - 0.0739200777362873j),
           (0.0979966872003005 - 0.0979966872003005j),
           (0.129915322011617 - 0.129915322011617j),
           (0.1722302189551 - 0.1722302189551j),
           (0.228327558766849 - 0.228327558766849j),
           (0.302696439734655 - 0.302696439734655j),
           (0.401288110479893 - 0.401288110479893j),
           (0.531992208939374 - 0.531992208939374j),
           (0.705268117796316 - 0.705268117796316j),
           (0.93498195955092 - 0.93498195955092j),
           (1.23951621039837 - 1.23951621039837j),
           (1.6432407279583 - 1.6432407279583j),
           (2.17846290945488 - 2.17846290945488j),
           (2.88801303858083 - 2.88801303858083j),
           (3.82867170921903 - 3.82867170921903j),
           (5.07571360002497 - 5.07571360002497j),
           (6.7289312080334 - 6.7289312080334j),
           (8.92062058076386 - 8.92062058076386j)]

test_circuits = [
    pytest.param('R-R-R', 3, id="Series"),
    pytest.param('R-p(R,R)', 1.5, id="Parallel"),
    pytest.param('R-p(R,R)-R', 2.5, id="Mix1"),
    pytest.param('R-p(R-R,R)-R', 2 + 2.0 / 3.0, id="Mix2"),
    pytest.param('R-p(R,C)', 1.0247045 - 0.1552231j, id="Randles"),
    pytest.param('R-p(R,CPE)', 1.2560427 - 0.1636903j, id="RandlesCPE"),
    ]

test_circuits2 = [
    pytest.param('R-R-R', 3, id="SeriesFreq"),
    pytest.param('R-p(R,R)', 1.5, id="ParallelFreq"),
    pytest.param('R-p(R,R)-R', 2.5, id="Mix1Freq"),
    pytest.param('R-p(R-R,R)-R', 2 + 2.0 / 3.0, id="Mix2Freq"),
    pytest.param('R-p(R,C)', reandles_res, id="RandlesFreq"),
    pytest.param('R-p(R,CPE)', randles_cpe_res, id="RandlesCPEFreq"),
    pytest.param('CPE', cpe_res, id="CPEFreq"),
    ]


@pytest.mark.parametrize(
        "circuit, expected",
        test_circuits
        )
def test_parse_circuit(circuit, expected):
    circuit_info, circuit_calc = parse_circuit(circuit)
    assert_array_almost_equal(
            circuit_calc(param_values, 1),
            expected
            )


@pytest.mark.parametrize(
        "circuit, expected",
        test_circuits2
        )
def test_parse_circuit_freq(circuit, expected):
    circuit_info, circuit_calc = parse_circuit(circuit)
    assert_array_almost_equal(
            circuit_calc(param_values, freq),
            expected
            )
