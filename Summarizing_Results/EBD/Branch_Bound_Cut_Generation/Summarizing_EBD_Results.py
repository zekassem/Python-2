import numpy as np
import csv
## End of Data
# Input parameters to the districting problem
probs_list=['CARP_F6_p_graph.dat','CARP_O12_g_graph.dat']
no_dist_list=[2,4,6,8,10,20,30,40,50]
tol_list=[0.01,0.1,1]


with open('Results/Summary_Branch_Cut_SPC_ECPM.csv', 'w') as newFile:
    newFileWriter = csv.writer(newFile, lineterminator='\n')
    newFileWriter.writerow(
        ['Instance_no','Instance_name', 'No. of Nodes', 'No. of Edges', 'No. of Districts', 'tolerance','No. of Threads',  'Time_Before_B&B&C','Time_for_B&B&C', 'Total_Time', 'Objective_Function_B&B&C','Sol_Status_B&B&C','gap'])
    i=1
    for prob in probs_list:
        graph_file = prob
        no_nodes = np.loadtxt(graph_file, skiprows=1, max_rows=1, usecols=1,
                                   dtype=int)  # skipping lines to get the number of nodes in the planar graph
        no_nodes1 = int(no_nodes)
        no_edges = np.loadtxt(graph_file, skiprows=2, max_rows=1, usecols=1,
                                   dtype=int)  # skipping lines to get the
        no_edges1 = int(no_edges)


        list_probs=[]
        for num in no_dist_list:
            for tol in tol_list:
                try:
                    results_file = 'EBD_Cut_Set_vs_SP_Contiguity_no_dist_'+str(num)+'_tol_'+str(tol)+'_prob_'+str(prob)+'.csv'
                    print(results_file)
                    num_threads = np.loadtxt(results_file, skiprows=1, max_rows=1, usecols=0, dtype=str, delimiter=',')
                    Time_Before_BBC=np.loadtxt(results_file, skiprows=3, max_rows=1, usecols=0, dtype=float,
                                                                 delimiter=',')

                    Time_For_BBC = np.loadtxt(results_file, skiprows=5, max_rows=1, usecols=0, dtype=float,
                                                       delimiter=',')

                    Total_Time=Time_Before_BBC+Time_For_BBC
                    Objective_Function_BBC = np.loadtxt(results_file, skiprows=3, max_rows=1, usecols=1, dtype=float,
                                                        delimiter=',')

                    Sol_Status_BBC = np.loadtxt(results_file, skiprows=7, max_rows=1, usecols=2, dtype=str,
                                               delimiter=',')
                    gap=round(np.loadtxt(results_file, skiprows=7, max_rows=1, usecols=1, dtype=float,
                                               delimiter=',')*100,2)
                    newFileWriter.writerow([i,prob, no_nodes1, no_edges1, num, tol,num_threads, Time_Before_BBC,Time_For_BBC,Total_Time,Objective_Function_BBC,Sol_Status_BBC,gap])
                    
                    i+=1
                except:
                    list_probs.append(results_file)
                    pass





print(list_probs)





