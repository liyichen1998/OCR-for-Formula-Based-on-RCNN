import alphabets

random_sample = True
keep_ratio = False
adam = False
adadelta = False
saveInterval = 1
valInterval = 300
n_test_disp = 10 #number of showing val set
displayInterval = 5
experiment = './expr'
alphabet = alphabets.alphabet
crnn = './trained_models/crnn_Rec_done_2_460.pth'
beta1 =0.5
lr = 0.000005 #0.0001 original
niter = 300
nh = 256
imgW = 180
imgH = 60
batchSize = 24
workers = 0
