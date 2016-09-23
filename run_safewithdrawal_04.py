#!/home/ubuntu/anaconda2/bin/python

# MIT License

# Copyright (c) 2016 Druce Vertes drucev@gmail.com

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from __future__ import print_function

import argparse
import pickle
from time import strftime
import sys
import os

import numpy as np
import pandas as pd

gamma = 4.0
fileprefix = "best%02.0f" % gamma
bestfile = "%s.pickle" % (fileprefix)

max_unimproved_steps = 2000

# startval = 100
# years_retired = 30
# const_spend_pct = .02
# const_spend = startval * const_spend_pct

# var_spend_pcts = pd.Series(np.ones(years_retired) * 0.02)
# var_spend_pcts[-1]=1.0
# stock_allocations = pd.Series(np.ones(years_retired) * 0.65)

startval = 100
years_retired = 30

#Objective: 7.203952

const_spend = 0.046854624598
var_spend_pcts = pd.Series([0.047728264432767613, 0.049411586294458174, 0.050928730122509078, 0.052344059676851309, 0.053732462146116412, 0.055217497823138666, 0.056941428407520825, 0.058930575848900338, 0.061336975451643787, 0.064041651590614299, 0.06682753017916232, 0.070015470233890598, 0.073482705866412062, 0.076908841885018162, 0.080315624573920857, 0.084248536285915637, 0.089148601519763754, 0.095047696579182661, 0.10188621415545694, 0.10924998386213798, 0.11753781748010764, 0.12760941026239583, 0.14057616911360005, 0.15671714345938417, 0.17824144932079172, 0.20888271848116302, 0.25566892685213716, 0.33619449575112598, 0.50043350250247753, 1.0000000001165821])
stock_allocations = pd.Series([0.99711355898839182, 0.99185701715221553, 0.99185701715220687, 0.98948774204807233, 0.98804540916535932, 0.98050079038519222, 0.97838578028389156, 0.97570008842349965, 0.96829250940421685, 0.96617128141912056, 0.96431002414689537, 0.96114519866116632, 0.96040289451991445, 0.95545525944604093, 0.94576492604012397, 0.94367216489810268, 0.93893019681658063, 0.93669535102064716, 0.9364792192199255, 0.92797207023216266, 0.92732340472916697, 0.92640611763229774, 0.92378045399910658, 0.92361726501803854, 0.92237182045552468, 0.91465926097427197, 0.90751802261070524, 0.89860934516344027, 0.89319891609596413, 0.8756356436940772])

#Objective: 5.531104

const_spend = 0.056242122011
var_spend_pcts = pd.Series([0.048748716423892849, 0.052068133447652862, 0.054288046668662264, 0.055362044561310976, 0.056967537716960129, 0.059394486706502693, 0.060974640720679867, 0.062924777341985982, 0.066918822882560305, 0.070501511745421089, 0.074000107422972847, 0.078266834437243527, 0.083532793810261574, 0.087183205070594572, 0.090006009028728851, 0.09421449518074819, 0.098897765019679451, 0.1054172063224097, 0.11257208133350892, 0.11980132773861227, 0.12642282208802053, 0.13543100666004262, 0.14772503811991666, 0.16220439640032858, 0.18284849431900019, 0.21239390728927757, 0.25776590041318476, 0.33721567782092066, 0.50098153958109037, 1.0000000001165821])
stock_allocations = pd.Series([0.99046452091874504, 0.98420301183001568, 0.97824162703543893, 0.96917932511020688, 0.96834109290983628, 0.96187983187090864, 0.95995295578689743, 0.95711230437687034, 0.95539300763466328, 0.95530524496135683, 0.95471371540553973, 0.95124894037767871, 0.95027006095402111, 0.94715100450155032, 0.93789570112960752, 0.9355385680515006, 0.93039340766996093, 0.92675524356154115, 0.91715296659062384, 0.90923034620927334, 0.90846733357214282, 0.90736125726257599, 0.90437784622535922, 0.89442023843006913, 0.89281058718535899, 0.88486056918161959, 0.87769635908398669, 0.86872376494698411, 0.86322499660079766, 0.855652751036732])

#Objective: 5.534285

const_spend = 0.057716260073
var_spend_pcts = pd.Series([0.048747677159537026, 0.052057769552692992, 0.054275681393732185, 0.055353720567914898, 0.056960438528937993, 0.059388015347947382, 0.060974703311745933, 0.062932214196815009, 0.066934303243626744, 0.07053396609151398, 0.074055318141031723, 0.07835725246628869, 0.083694343720676981, 0.087417862043279213, 0.090308934982966327, 0.094621933303298975, 0.099413544604790668, 0.10610428732329681, 0.11344033806112135, 0.12083494756346039, 0.127470991290518, 0.13651027345340919, 0.14884874757995939, 0.16318630190900693, 0.1837601787219697, 0.21314798687758532, 0.25824774792122618, 0.3374601065412125, 0.50111485848226534, 1.0000000001165821])
stock_allocations = pd.Series([0.98916085498421158, 0.98269622850287897, 0.9775441950881768, 0.9691651508503889, 0.9684475826036778, 0.9619912144750834, 0.9605030716080335, 0.95743266819987005, 0.95512026690407681, 0.95506665065160801, 0.95455723646441593, 0.95127145017934944, 0.9502402076675891, 0.94749192805241966, 0.93832568543062522, 0.93593362553835602, 0.93070936636852397, 0.92675821852148188, 0.91729914157782444, 0.90951926215736756, 0.90873436649878336, 0.90758622069079309, 0.90452262133003036, 0.89462069590027649, 0.8929220703095665, 0.88491303035728719, 0.87774282567413575, 0.86875409988588492, 0.86323228280148756, 0.85565737506009365])

#Objective: 5.540341

const_spend = 0.061253727606
var_spend_pcts = pd.Series([0.048735800528412442, 0.05202211739379492, 0.054234161059465963, 0.055324590403038686, 0.056935488744175346, 0.059359466592334938, 0.060956059784111845, 0.062923003854180079, 0.066921670533768601, 0.070533928539214474, 0.074078265904014617, 0.078411282814850741, 0.083814697172533231, 0.087632408838270268, 0.090629174869846521, 0.095101701373187561, 0.10007897392769673, 0.10706698779469195, 0.11476336046224861, 0.12253641332490567, 0.12933219713386018, 0.13856492325810627, 0.15112878336960808, 0.16530848550217667, 0.18583982601137664, 0.21495646028304632, 0.25945416207886546, 0.3380895789094181, 0.50146257776475689, 1.0000000001165821])
stock_allocations = pd.Series([0.98590733785663043, 0.97894553841833409, 0.97582163965821334, 0.96913695313708181, 0.96872096167260868, 0.96227992049514521, 0.96188367803293295, 0.95824519629001004, 0.95459797678555758, 0.95447114455531967, 0.95402774269199153, 0.95133700140185018, 0.95017317622144148, 0.94834781784075539, 0.93939857653686687, 0.93692451989794101, 0.93150668372620904, 0.92676171690426168, 0.91766435302464389, 0.91025742957652744, 0.90942046373259866, 0.90816658160731156, 0.90489960471550368, 0.8951475825830908, 0.89321779081815011, 0.88505326394892969, 0.87786757148086991, 0.86883603546972088, 0.86325222101752541, 0.85567002280416116])

#Objective: 5.542092

const_spend = 0.062428699945
var_spend_pcts = pd.Series([0.048729836781967045, 0.052007889696062445, 0.054217707925869295, 0.055312139741597731, 0.056924196164180971, 0.0593464601319268, 0.060945799172557658, 0.062915044158072267, 0.066910127429727601, 0.070523552461770694, 0.074071498583898276, 0.078407200216925377, 0.083816394967718061, 0.087649787838133583, 0.090667679226685338, 0.095171075321442603, 0.10018791115922246, 0.10724204640506624, 0.11503024399271977, 0.12291178460831542, 0.12977764033161679, 0.13909354861578424, 0.15175441556369124, 0.16592750112546092, 0.18647906877185902, 0.21553992048543719, 0.25985998520409997, 0.33830731428328842, 0.50158441930215125, 1.0000000001165821])
stock_allocations = pd.Series([0.98479828529470359, 0.97767019663687138, 0.97523928178427921, 0.96912876571572992, 0.96881577953215003, 0.96238094310615729, 0.96235562455973178, 0.95852517818896676, 0.95421498494413903, 0.95416791459038519, 0.95415739764129637, 0.95136221505265506, 0.95015289873614905, 0.94864153211432645, 0.93976471816761775, 0.93726374560526304, 0.93178088760361055, 0.92676215806854501, 0.91778873621610202, 0.91051313760318975, 0.90965909156609803, 0.90836893398475205, 0.90503194135699294, 0.89533398174600709, 0.89332323378633327, 0.88510358852903037, 0.87791250143751809, 0.86886571932457934, 0.86325953200698391, 0.85567465670987886])

#Objective: 5.542204

const_spend = 0.062508598487
var_spend_pcts = pd.Series([0.048729407697117519, 0.052006894959283352, 0.054216558986737509, 0.055311260811870301, 0.056923392297000282, 0.059345534546941005, 0.060945055520964894, 0.062914449941118764, 0.066909263008743156, 0.07052274761667876, 0.07407091094384978, 0.078406727767937695, 0.083816150183045626, 0.087650432581576801, 0.090669584215410409, 0.095174780026976435, 0.10019396257487835, 0.10725208868838303, 0.1150460326802997, 0.12293455847932376, 0.12980527333888811, 0.13912698606743612, 0.15179467344991926, 0.16596797516764897, 0.18652144961525918, 0.21557910721402565, 0.25988755266265151, 0.33832222022145508, 0.50159279121529643, 1.0000000001165821])
stock_allocations = pd.Series([0.9847224767323306, 0.977583078418504, 0.97519954893339378, 0.9691282244077325, 0.96882228776854662, 0.96238789369615363, 0.96238789355139487, 0.95854435524858039, 0.95421201221659591, 0.95415402147609008, 0.95413630060753285, 0.95136398849082027, 0.95015156600200545, 0.94866164878389436, 0.93978975545434595, 0.93728695998906397, 0.93179967733117319, 0.92676218075446337, 0.91779723292023141, 0.91053068025661743, 0.90967547722488284, 0.90838283372169715, 0.90504104452096656, 0.89534682918963882, 0.89333051650821682, 0.885107069655931, 0.8779156118219863, 0.86886777786794134, 0.86326004071970186, 0.85567497902547474])

bond_allocations = 1 - stock_allocations


# save starting scenario
pickle_list = [const_spend, var_spend_pcts, stock_allocations, bond_allocations]
pickle.dump( pickle_list, open( bestfile, "wb" ) )


# start with a learning rate that learns quickly, gradually reduce it
# run once with 50 or 100 steps to see which learning rates are effective
# then plug in that solution and run each til no improvement for a large number of steps

for learning_rate in [
        #0.00001, # too coarse, may be NaN
        0.00003, # too coarse, may be NaN
        0.000001, # coarse
        0.000003, # coarse
        0.0000001, # workhorse
        0.00000003, 
        0.00000001, # diminishing returns
        0.000000003,
        #0.000000001, #superfine
        #0.0000000003, 
        #0.0000000001, 
        #0.00000000001, 
]:
    cmdstr = './safewithdrawal.py %.12f %d %f %s' % (learning_rate, max_unimproved_steps, gamma, fileprefix)
    print(cmdstr)
    os.system(cmdstr)

