Load_Airfoil_Variables.m
% This script loads variables for Bezier_Airfoil_Generator which calls
% the Bezier function and the Add_thickness script %
% The number of points on the leading edge is defined in Add_Thickness.m
% The number of points that span the upper and lower surface is defined in
% Bezier.m
outputfolder = 'c:\mike\temp\'; %Fill in folder where airfoil files should be dumped airfoilnames = 'Airfoilnames.out'; % note that airfoil name file must be in above folder and be named "Airfoilnames.out"
144
Cv = [0.07];%[0.06 0.07 0.08]; % set of max camber values
XCv = [0.30];%[0.20 0.25 0.30 0.35]; % set of max camber location values Rv = [0.02];%[0.01 0.02 0.03]; % set of max reflex values
XRv = [0.85];%[0.75 0.80 0.85]; %set of max reflex location values
Tv = [0.01];%[0.01 0.015]; %set of thickness values
global parameters;
global controlpoints;
global checkpoints; [controlpoints,parameters,checkpoints]=Bezier_Airfoil_Generator(outputfolder,airfoilnames, Cv,XCv,Rv,XRv,Tv)
max_C_err = max(abs(checkpoints(:,1)-parameters(:,1))) max_XC_err = max(abs(checkpoints(:,2)-parameters(:,2))) max_R_err = max(abs(checkpoints(:,3)+parameters(:,3))) max_XR_err = max(abs(checkpoints(:,4)-parameters(:,4)))

