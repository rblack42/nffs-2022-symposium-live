Load_variables.m
% This script loads the variables for SavePolarData_X
% It is assumed that it will be used only for Bezier Airfoils that follow % the standard naming convention
% This section matches the section in the Expect script
directory = 'C:\Mike\Thesis\Thin Airfoil Work\Collected Data\Data 12\'; airfoil_dir = 'C:\Mike\Thesis\Thin Airfoil Work\Collected Data\Airfoils\'; airfoil_file = 'Airfoilnames.out';
airfoil_read_start = [1];
airfoil_read_stop = [432];
airfoil_read_size = [12]; % 12 for Bezier Airfoils
airfoil_row_size = [17]; % 17 for Bezier Airfoils, 18 if*
reynolds_nums = ['060';'100';'150'];
reynolds_nums_values = [60 100 150];
AOA_min = [0];
AOA_step = [0.2];
AOA_max = [12];
AOA_BL_range = ['00';'01';'02';'03';'04';'05';'06';'07';'08';'09';'10';'11';'12';'13';'14']; AOA_CP_range = ['00';'01';'02';'03';'04';'05';'06';'07';'08';'09';'10';'11';'12';'13';'14']; AOA_H_range = ['00';'01';'02';'03';'04';'05';'06';'07';'08';'09';'10';'11';'12';'13';'14']; Ncrit = ['7'];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % This section pulls the information from Airfoilnames.out to use in
% opening data files
i = 0;
[fid] = fopen([airfoil_dir airfoil_file],'r');
for count_airfoil_read = airfoil_read_start:airfoil_read_stop
i = i+1;
fseek(fid,[airfoil_row_size * (count_airfoil_read - 1)],'bof'); airfoilnames(i,:) = char(fread(fid,12,'12*uchar=>uchar')); airfoilnumbers(i,:) = count_airfoil_read;
end fclose(fid);
% this section collects the camber, Xcamber, reflex, Xreflex, and Thickness values % from the airfoilnames.out file and saves them to the data_parameters matrix
i = 0;
[fid] = fopen([airfoil_dir airfoil_file],'r');
for count_airfoil_read = airfoil_read_start:airfoil_read_stop i = i+1;
155
fseek(fid,[airfoil_row_size * (count_airfoil_read - 1) + 3],'bof'); saved_par_char(i,:) = (fread(fid,9,'int8=>int8'));
data_parameters(i,1) = char_convert(saved_par_char(i,1:2)); % Camber data_parameters(i,2) = char_convert(saved_par_char(i,3:4)); % Xcamber data_parameters(i,3) = char_convert(saved_par_char(i,5)); % Reflex data_parameters(i,4) = char_convert(saved_par_char(i,6:7)); % Xreflex data_parameters(i,5) = char_convert(saved_par_char(i,8:9)); % Thickness
end
fclose(fid); %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
[Name_Polar_Data,Missing_Polar_Files, Missing_Polar_Files_num,data_eval]=SavePolarData_x_v3(directory, airfoilnames, airfoilnumbers, data_parameters, reynolds_nums, reynolds_nums_values, Ncrit) [P_data_matrix]=RetrevePolarData_X(directory, airfoilnames, airfoilnumbers, data_parameters, AOA_min, AOA_step, AOA_max, reynolds_nums, reynolds_nums_values, Ncrit, data_eval)
[Name_BL_Data, Missing_BL_Files, Missing_BL_Files_num]=SaveBLData_X(directory, airfoilnames, airfoilnumbers, AOA_BL_range, reynolds_nums, Ncrit) [BL_data_matrix]=RetreveBLData_X(directory, airfoilnames, airfoilnumbers, data_parameters, AOA_BL_range, reynolds_nums, reynolds_nums_values, Ncrit, Missing_BL_Files)
[Name_CP_Data, Missing_CP_Files]=SaveCPData_X(directory, airfoilnames,airfoilnumbers, AOA_CP_range, reynolds_nums, Ncrit)
[Name_H_Data, Missing_H_Files]=SaveHData_X(directory, airfoilnames, airfoilnumbers, AOA_H_range, reynolds_nums, Ncrit)

