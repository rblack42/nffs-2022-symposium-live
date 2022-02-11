Bezier_Airfoil_Generator.m
function [controlpoints,parameters,checkpoints] = Bezier_Airfoil_Generator (outputfolder,airfoilnames,Cv,XCv,Rv,XRv,Tv)
% function [controlpoints,parameters,checkpoints]=Bezier_Airfoil_Generator(outputfolder,airfoilnames, Cv,XCv,Rv,XRv,Tv)
%
% The function generates the airfoil parameter matrix, bezier control points
% matrix, output airfoil names file, checkpoints matrix for validation, and
% the output airfoil coordinate files.
% The coordinates for each airfoil are saved as its own file from the names
% listed in sequence in the file 'airfoilnames'in the folder 'outputfolder' %
% Inputs:
% outputfolder = Folder where all files will be dumped
% airfoilnames = File that contains all the airfoil file names
% Cv = Vector of all Max Camber values
% XCv = Vector of all Max Camber location values
% Rv = Vector of all Max Reflex values
% XRv = Vector of all Max Reflex location values
% Tv = Vector of all Thickness values %
% Outputs:
% controlpoints = Array of all Bezier control points for the corresponding control points
% parameters = Array of all combinations of airfoil parameters
145
[Cvn,Cvm] = size(Cv); [XCvn,XCvm] = size(XCv); [Rvn,Rvm] = size(Rv); [XRvn,XRvm] = size(XRv); [Tvn,Tvm] = size(Tv);
% Constants outside of loops
n = 0; % acts as counter, n represents the number of the airfoil in the sequence
nn = 0; % acts as counter, nn represents the number of the airfoil in the sequence for the first loop group
% This section creates the file Airfoilnames.out which contains a list of % all the airfoil names in the format of the airfoil naming convention % BEZCvXCvRvXRvTv
% this section generates the matrix that contains all possible parameter combinations for i = 1:Cvm
for j = 1:XCvm for k = 1:Rvm
for l = 1:XRvm for m = 1:Tvm
nn = nn+1; % indicates what airfoil is being calculated! global parameters;
parameters(nn,:) = [Cv(i),XCv(j),Rv(k),XRv(l),Tv(m)];
end end
end end
end
% Creates the airfoilnames file
fid = fopen([outputfolder airfoilnames],'a');
var = [parameters(:,1:4)*100 parameters(:,5)*1000]'; fprintf(fid,'BEZ%02.0f%01.0f%01.0f%01.0f%02.0f.cor\n',var); % Set the file extension here (.cor)
fclose(fid);
for i = 1:Cvm
for j = 1:XCvm
for k = 1:Rvm
for l = 1:XRvm
for m = 1:Tvm
n = n+1; % indicates what airfoil is being calculated! n_prime = nn - n;
146

[x1,y1,x2,y2,x,y]=Bezier(Cv(i),XCv(j),Rv(k),XRv(l),Tv(m)); % call bezier function to generate x1,y1,x2,y2 control points
global checkpoints
[C_chk,Cx_chk_num] = max(y);
[R_chk,Rx_chk_num] = min(y);
checkpoints(n,:) = [C_chk,x(Cx_chk_num),R_chk,x(Rx_chk_num)];
global controlpoints;
controlpoints(n,:) = [x1 y1 x2 y2]; % matrix contains all x1 y1 x2 y2 values corresponding to the C XC R XR values in
run Add_Thickness
% generate a file of the airfoil coordinates
fid = fopen([outputfolder 'Airfoilnames.out'],'r'); position = -(16*(n_prime+1)+(n_prime+1)); fseek(fid, position, 'eof');
s = fread(fid,16,'16*uchar=>uchar');
f = char(s');
fclose(fid);
% Generates the actual airfoil coordinate file
fid = fopen([outputfolder f],'w');
var = [parameters(n,1:4)*100 parameters(n,5)*1000]'; fprintf(fid,'BEZ%02.0f%01.0f%01.0f%01.0f%02.0f\n',var);
fprintf(fid,'%-1.6f
fclose(fid); end
end end
end end

