SavePolarData_X_v3.m
function [Name_Polar_Data,Missing_Polar_Files, Missing_Polar_Files_num, data_eval]=SavePolarData_X(directory, airfoilnames, airfoilnumbers, data_parameters, reynolds_nums, reynolds_nums_values, Ncrit)
% [Name_Polar_Data,Missing_Polar_Files, Missing_Polar_Files_num]=SavePolarData_X(directory, airfoilnames, airfoilnumbers, data_parameters, reynolds_nums, reynolds_nums_values, Ncrit)
%
% This function takes the imput matricies airfoilnames,,
% reynolds_nums, and Ncrit to form filenames that correspond to
% polar files in the given directory. The data is then
% evaluated for quality and a quality file is created %
156
% Note that all polar files should follow the standard naming format:
% i.e. BEZ032518510_Re060K_N7_X_P.txt or airfoilname_ReZZZK_NY_X_P.txt % Reynolds number must be displayed as 3 digits
% The N7 shows the Ncrit value used
% The X means the data was collected with XFOIL
% the P means it is a polar file
% Data files generated will have a D after the X to read XD to note that it
% is a data file.
%
% Inputs:
% directory = location of the polar data files
% airfoilnames = A column vector that contains all the airfoil names that have polars % reynolds_num = A column vector that contains all the reynolds numbers tested
% Ncrit = N value for run
%
% Outputs:
% Name_Polar_Data = contains names of the polar files, each row has the name of % corresponding column's data in the other variables.
% Missing_Polar_Files = List of missing Polar files
% Constants
i = 0; % counter
position = 0; % current location in the file
hit = 0; % flag for successful find
count = 0; %counter for where the data is going in mfcount = 0; %counter for missed files no_data_count = 0; %counter for empty data files
fclose('all');
[j,z] = size(airfoilnames); [k,z] = size(reynolds_nums);
for airfoilnum = 1:j for ren_num = 1:k
count = count+1;
filename = [airfoilnames(airfoilnum,:) '_Re'reynolds_nums(ren_num,:) 'K_N'Ncrit '_X_P .txt'];
[fid] = fopen([directory filename],'r');
if fid == -1
mfcount = mfcount+1;
Missing_Polar_Files(mfcount,:) = [airfoilnames(airfoilnum,:) '_Re'
reynolds_nums(ren_num,:) 'K_X_P.txt']; Missing_Polar_Files_num(mfcount,:) = [airfoilnumbers(airfoilnum,:)];
157

data_eval(count,:) = [data_parameters(airfoilnum,:) reynolds_nums_values(ren_num) 0 0 0 0 0 0 0];
end
if fid ~= -1 % All of the following code will be skipped if the file does not open properly and there will be a column of 0's it it's place.
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % Search for airfoil name from Polar file %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
position = 1; i = 0;
hit = 0; while hit < 1
position = position+1;
fseek(fid, position, 'bof');
chnameseek(1) = fread(fid,1,'1*uchar=>uchar');
fseek(fid, position+1, 'bof');
chnameseek(2) = fread(fid,1,'1*uchar=>uchar');
fseek(fid, position+2, 'bof');
chnameseek(3) = fread(fid,1,'1*uchar=>uchar');
if chnameseek == [114 58 32] % find the position in the file that corresponds to the
sequence 'r: '
hit = 1;
end end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % Get airfoil name from Polar file % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
i = 0;
hit = 0;
position = position+2; % adjust the position found above to correspond to the start of
the airfoil name while hit < 1
i = i+1;
fseek(fid, position+i, 'bof');
chaf(i,:) = fread(fid,1,'1*uchar=>uchar');
if chaf(i,:) == [32]; % copy letters for the airfoil name until there is 3 spaces in a
row
hit = 1;
end
158

if chaf(i,:)~= [32];
airfoilname(i) = char(chaf(i,1)');
end end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % Search for Reynolds number from Polar file %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% position = 1;
i = 0;
hit = 0; while hit < 1
position = position+1;
fseek(fid, position, 'bof');
chreseek(1) = fread(fid,1,'1*uchar=>uchar');
fseek(fid, position+1, 'bof');
chreseek(2) = fread(fid,1,'1*uchar=>uchar');
fseek(fid, position+2, 'bof');
chreseek(3) = fread(fid,1,'1*uchar=>uchar');
if chreseek == [82 101 32] % find the position in the file that corresponds to the
sequence 'Re '
hit = 1;
end end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % Get Reynolds number from Polar file % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
position = position+11; % adjust the position found above to correspond to the start of the Reynolds number
i = 0;
hit = 0; while hit < 1
fseek(fid, position+i, 'bof');
i = i+1;
chre(i) = fread(fid,1,'1*uchar=>uchar'); if chre(i) == 32;
hit = 1; end
if chre(i) ~= 32;
renumber(i) = char(chre(i));
end end
159

renumberout = ['_Re'renumber 'K'];
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % Search for Ncrit number from Polar file %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% position = 1;
i = 0;
hit = 0; while hit < 1
position = position+1;
fseek(fid, position, 'bof');
chNseek(1) = fread(fid,1,'1*uchar=>uchar');
fseek(fid, position+1, 'bof');
chNseek(2) = fread(fid,1,'1*uchar=>uchar');
fseek(fid, position+2, 'bof');
chNseek(3) = fread(fid,1,'1*uchar=>uchar');
if chNseek == [78 99 114] % find the position in the file that corresponds to the
sequence 'Re '
hit = 1;
end end
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % Get Reynolds number from Polar file % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
position = position+10; % adjust the position found above to correspond to the start of the Reynolds number
i = 0;
hit = 0; while hit < 1
fseek(fid, position+i, 'bof');
i = i+1;
chN(i) = fread(fid,1,'1*uchar=>uchar'); if chN(i) == 46;
hit = 1; end
if chN(i) ~= 46;
Nnumber(i) = char(chN(i));
end end
Ncritout = ['_N'Nnumber];
160

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% % Get Polar data to output to data file from Polar file %
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
position = 1; i = 0;hit = 0; while hit < 1
position = position+1;
fseek(fid, position, 'bof');
datastart(1) = fread(fid,1,'1*uchar=>uchar');
fseek(fid, position+1, 'bof');
datastart(2) = fread(fid,1,'1*uchar=>uchar');
fseek(fid, position+2, 'bof');
datastart(3) = fread(fid,1,'1*uchar=>uchar');
if datastart == [45 45 13] % Search for the start of the data which comes after the
last '--(new line)' hit = 1;
end end
% This gets all the data from the file fseek(fid, position+4, 'bof');
polardata = char(fread(fid, 50000, 'uchar')'); fclose(fid);
% This section creates the easy to read txt file
filename = [directory 'Data Files\'airfoilname renumberout Ncritout '_XD_P.txt']; % Creates the file name from the airfoil name and the reynolds number.
fid = fopen(filename,'w'); fwrite(fid, polardata, 'uchar'); fclose(fid);
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This section analyzes the data and creates data_eval and % finds the stall point, stall behavior, Cl_max, Cl_Cd_max
[data]=load(filename);% Get polar data from file AOA = data(:,1);
Cl = data(:,2);
Cd = data(:,3);
Cl_Cd = Cl./Cd;
[max_AOA_gap,AOA_n] = max(diff(AOA));
161

stall_catch = 0; i = 0;
m = find(diff(sign(diff(Cl)))<0)+1;
if length(find(sign(diff(Cl))>0))==(length(diff(Cl))) m = 1;
end
%plot(AOA,Cl,'.',AOA(m),Cl(m),'x')
while stall_catch == 0 i = i+1;
low_range = min(m(i) - round(0.5*m(i)))+1;
high_range = max(m(i) + round(0.5*(length(AOA)-m(i))));
%plot(AOA(low_range:high_range),Cl(low_range:high_range),'.',AOA(m(i)),Cl(m(i)),'x')
if max(Cl(low_range:high_range)) == Cl(m(i)) stall_catch = 1;
max_Cl = Cl(m(i));
max_Cl_AOA = AOA(m(i));
max_Cl_AOA_error = AOA(m(i)+1)-AOA(m(i)-1);
[Cl_Cd_max,q] = max(Cl./Cd); Cl_Cd_max_AOA = AOA(q); Cl_CD_AOA_error = AOA(q+1)-AOA(q-1);
elseif i == length(m)
stall_catch = 1; %no stall point!!!
max_Cl = 0; max_Cl_AOA = 0; max_Cl_AOA_error = 0;
Cl_Cd_max = 0; Cl_Cd_max_AOA = 0; Cl_CD_AOA_error = 0;
end end
162

if max_AOA_gap > 2 & AOA(AOA_n-1) < max_Cl_AOA
max_Cl = 0; max_Cl_AOA = 0; max_Cl_AOA_error = 0;
Cl_Cd_max = 0; Cl_Cd_max_AOA = 0; Cl_CD_AOA_error = 0;
end
%figure(1)
%plot(AOA,Cl,'.',max_Cl_AOA,max_Cl,'x')
%figure(2)
%plot(Cd,Cl,'.',Cd(nn(i)),Cl(nn(i)),'x')
data_eval(count,:) = [data_parameters(airfoilnum,:) reynolds_nums_values(ren_num)
1 max_Cl_AOA max_Cl max_Cl_AOA_error Cl_Cd_max_AOA Cl_Cd_max Cl_CD_AOA_error];
% Creates a check variable to compair with to be sure correct data was collected
Name_Polar_Data(count,:) = [airfoilname renumberout Ncritout '_XD_P.txt']; end
end end
if mfcount == 0
Missing_Polar_Files = ['No missing files!']; Missing_Polar_Files_num = [0];
end
% Generate list of airfoils to rerun in xfoil % camber_values = [3 4 5 6 7 8];
% camber_char = ['03';'04';'05';'06';'07';'08']; % for i = 1:length(camber_values)
% var = data_eval(find(data_eval(:,7)==0 & data_eval(:,1)==camber_values(i) & data_eval(:,6)==60),1:5)';
% fid = fopen(['C:\Mike\temp\Missing Airfoils\''Missing_Airfoils_C'camber_char(i,:) 'K.out'],'w');
% fprintf(fid,'BEZ%02.0f%01.0f%01.0f%01.0f%02.0f.cor\n',var); % Set the file extension here (.cor)
% fclose(fid);
% end
%Generate list of airfoils to rerun in xfoil % for i = 1:length(reynolds_nums_values)
163

% var = data_eval(find(data_eval(:,8)==0 & data_eval(:,6)==reynolds_nums_values(i)),1:5)';
% fid = fopen(['C:\Mike\temp\Missing Airfoils\''Mising_Airfoils_Re'reynolds_nums(i,:) 'K.out'],'w');
% fprintf(fid,'BEZ%02.0f%01.0f%01.0f%01.0f%02.0f.cor\n',var); % Set the file extension here (.cor)
% fclose(fid);
% end
