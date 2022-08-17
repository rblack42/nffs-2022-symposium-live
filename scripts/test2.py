from subprocess import Popen, PIPE, STDOUT
#import numpy as np
#import itertools as itr
#import csv


def xfoil_interact(foil, re, alpha_start, alpha_end, alpha_step):

    def cmd(foil, re, alpha_start, alpha_end, alpha_step):

        load_cmd = 'LOAD ' + foil
        cmd = f'''
            LOAD {foil}

            PLOP
            G F

            OPER
            VISC {re}
            ITER 200
            PACC
            output/{re}_save
            
            ASEQ
            {alpha_start}
            {alpha_end}
            {alpha_step}

        '''
        return cmd

    ps = Popen('xfoil', stdin=PIPE, stdout=PIPE, stderr=STDOUT)
    stdout = ps.communicate(input=cmd(foil=foil, re=re, alpha_start=alpha_start,
                alpha_end=alpha_end,alpha_step=alpha_step).encode())[0]
    print(stdout)
    print('====================================')
    return None

re_start = 3000
re_end = 6000
re_step = 500
re_num = int((re_end-re_start)/re_step) + 1

alpha_start = -10
alpha_end = 20
alpha_step = 2
alpha_num = int((alpha_end-alpha_start)/alpha_step) + 1

foil = 'flat0001.dat'

#tbl = np.zeros([int(re_num*alpha_num), 4])

i = 0
for re in range(re_start, re_end+re_step, re_step):
    xfoil_interact(foil, re, alpha_start, alpha_end, alpha_step)
    i = i + 1
    #tbl_end = alpha_num*i

    #if i == 1:
    #    tbl_start = 0
    #else:
    #    tbl_start = alfa_num*i-alfa_num

    aa_list = []
    cl_list = []
    cd_list = []
    cm_list = []
    #tbl[tbl_start:tbl_end,0] = re  # stores set of Reynolds

    #with open('output/{}_save'.format(re),'r') as infile:
    #    for x in itr.islice(infile, 12, None): # ignores first 13 lines
    #        x = x.split()
    #        aa_list.append(float(x[0]))
    #        cl_list.append(float(x[1]))
    #        cd_list.append(float(x[2]))
    #        cm_list.append(fload(x[3])))

    #tbl[tbl_start:tbl_end,1] = aa_list
    #tbl[tbl_start:tbl_end,2] = cl_list
    #tbl[tbl_start:tbl_end,3] = cd_list

#outfile = open('output/outfile.csv', 'w+', newline = '')
#with outfile:
#    write = csv.writer(outfile)
#    write.writerows(tbl)
