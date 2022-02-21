Expfoil_V4.tcl
######################################## # Xfoil Expect script Expfoil_V4.tcl #
# Written by: Michael Reid
# On: June 14, 2006
# Updated on: July 18, 2006
# Validated on : July 19, 2006 ########################################
# This script was designed to: #
# If the option is set:
# Set the number of panels for every airfoil using the XFOIL default setting
# Run an airfoil through the AOA range initilizing only at failed AOA
# Set N_crit value to be used for all calculations
# Set Vacc, Tgap, blend, iter, and TE_LE for all data collected.
# Improve LE panel density.
# Read in the airfoil names from an outside file to be run
# Save BL, CP, and H data files for specific AOA
# File location:
# cd F:/mike/test\ scripts/
# tclsh Expfoil_V4_lab.tcl
# required for expect package require Expect
####### Set variables ####### # Folder locations
  #
#
#
#
137
set output_folder "Z:/Data/" set airfoil_folder "Z:/Airfoils/" set xfoil_dir "E:/xfoil/"
# File names
set airfoil_file Airfoilnames.out
# Airfoil read variables: set airfoil_read_start 1 set airfoil_read_stop 432 set airfoil_read_size 12 set airfoil_row_size 17
# Analysis Re numbers
set Re {60000 100000 150000}
set Re_name {Re060K Re100K Re150K}
# Analysis AOA range set AOA_min "0"
set AOA_step ".2"
set AOA_max "12"
# BL, CP, and H record AOA lists
set AOA_BL {0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0} set AOA_BL_name {00 02 04 06 08 10 12 14 16 18}
set AOA_CP {0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0} set AOA_CP_name {00 02 04 06 08 10 12 14 16 18}
set AOA_H {0.0 2.0 4.0 6.0 8.0 10.0 12.0 14.0 16.0 18.0} set AOA_H_name {00 02 04 06 08 10 12 14 16 18}
####### Set XFOIL variables #######
set panel_flag 1 set TE_gap_flag 1 set n 250
set TE_gap 0.001 set blend_dist 0.8 set iter 400
set N_crit 7
set Vacc 0.001
set TE_LE 0.1
####### script variables #######
set timeout 5
set count_airfoil_read $airfoil_read_start
138

####################### Set procedures #########################
proc set_current_airfoil {count_airfoil_read} {
global airfoil_folder airfoil_row_size airfoil_read_size current_airfoil airfoil_file
set airfoil_ch_id [open "$airfoil_folder$airfoil_file" r]
set airfoil_loc [expr $airfoil_row_size * ($count_airfoil_read - 1)] seek $airfoil_ch_id $airfoil_loc
set current_airfoil [read $airfoil_ch_id $airfoil_read_size]
close $airfoil_ch_id
}
proc load_airfoil {current_airfoil} { global airfoil_folder
# load airfoil
expect "XFOIL c>" {send "load $airfoil_folder/$current_airfoil.cor\r"} }
proc panel {n TE_LE} {
# open panel menu
expect "XFOIL c>" {send "ppar\r"}
# Choose number of panels
expect "else) c>" {send "n\r"}
# Send number of panels
expect "nodes i>" {send "$n\r"}
# Choose TE/LE panel ratio
expect "else) c>" {send "t\r"}
# Send TE/LE panel ratio
expect "panel density ratio r>" {send "$TE_LE\r"} # No more changes
expect "else) c>" {send "\r"}
# Return to main menu
expect "else) c>" {send "\r"}
}
proc set_TE_gap {TE_gap blend_dist} { # open geometric design menu
expect "XFOIL c>" {send "gdes\r"}
# Call TE gap sub menu
expect ".GDES c>" {send "tgap\r"}
# Send TE gap value
expect "Enter new gap r>" {send "$TE_gap\r"}
# Send blending distance
expect "Enter blending distance/c (0..1) r>" {send "$blend_dist\r"}
139

# Return to main menu
expect ".GDES c>" {send "\r"}
# Set buffer airfoil to current airfoil expect "XFOIL c>" {send "pcop\r"}
}
proc iter_set {iter} {
# call iteration limit prompt expect "c>" {send "iter\r"}
# Send iteration limit
expect "limit i>" {send "$iter\r"}
}
proc set_vpar {} { global N_crit Vacc
expect "c>" {send "vpar\r"} expect "c>" {send "n\r"} expect "r>" {send "$N_crit\r"} expect "c>" {send "vacc\r"} expect "r>" {send "$Vacc\r"} expect "c>" {send "\r"}
}
proc visc_Re {Re count_Re Re_name} { global current_Re_name current_Re
# get Re number for current loop
set current_Re [lindex $Re $count_Re]
# get Re number name for current run
set current_Re_name [lindex $Re_name $count_Re] # loop actions:
# Set viscious solution and Reynolds number
expect ".OPERi c>" {send "visc $current_Re\r"}\
".OPERv c>" {send "re $current_Re\r"} }
proc pacc_on {current_airfoil current_Re_name} { global current_output_P_file N_crit output_folder
# set current output polar file name
set current_output_P_file "$current_airfoil\_$current_Re_name\_N$N_crit\_X_P.txt" # Turn on polar accumulation
expect "c>" {send "pacc\r"}
# Send polar save file
expect "s>" {send "$output_folder$current_output_P_file\r"}
140

# Don't set polar dump file
expect "s>" {send "\r"} }
proc alfa {current_AOA} {
global converged_AOA converged_failed failed_reason timeout iter current_airfoil
set timeout 60
expect "c>" {send "alfa $current_AOA\r"} expect "Point added*c>" {set converged_AOA 1
send "cpmn\r"}\ "VISCAL*c>" {set converged_AOA -1
set failed_reason "failed AOA: $current_AOA"
send "init\r"}\
"STFIND*Continuing" {set converged_failed 1
set failed_reason "$current_airfoil\n locked $current_AOA"}\ "BL array overflow" {set converged_failed 1
set failed_reason "$current_airfoil\n BL_array_overflow
$current_AOA"}\
timeout {set converged_failed 1
}
set failed_reason "$current_airfoil\n timeout $current_AOA"}
proc set_par {par AOA_par AOA_par_name} {
global current_AOA AOA_step count_AOA_par converged_AOA current_AOA_par_name
global current_output_AOA_par_file par_data current_airfoil current_Re_name N_crit
set count_AOA_par [lsearch $AOA_par [expr $current_AOA - $AOA_step]] set par_data -1
if {$count_AOA_par != -1} {
set par_data 1
set current_AOA_par_name [lindex $AOA_par_name $count_AOA_par] set current_output_AOA_par_file
"$current_airfoil\_$current_Re_name\_N$N_crit\_$current_AOA_par_name\_X\_$par.txt"
} }
proc pacc_off {} {
# Turn off polar accumulation
expect "c>" {send "pacc\r"}
# Remove polar data for this airfoil from RAM expect "c>" {send "pdel 0\r"}
}
proc missing_rec {failed_reason missing_file} {
141

global output_folder current_airfoil
set failed_ch_id [open "$output_folder$missing_file" a] puts $failed_ch_id $failed_reason\r
close $failed_ch_id
}
proc x_reset {} {
global xfoil_dir airfoil airfoil_folder count_airfoil_read n panel_flag TE_gap blend_dist
TE_gap_flag
global iter Re count_Re Re_name current_airfoil current_Re_name output_folder TE_LE
Vacc N_crit
load_airfoil $current_airfoil
if {$TE_gap_flag == 1} {set_TE_gap $TE_gap $blend_dist} if {$panel_flag == 1} {panel $n $TE_LE}
expect "XFOIL c>" {send "oper\r"}
iter_set $iter
visc_Re $Re $count_Re $Re_name
set_vpar
pacc_on $current_airfoil $current_Re_name
}
################# End procedures #################
# Start xfoil
spawn "$xfoil_dir./xfoilP4.exe"
################# Airfoil Loop ################# while {$count_airfoil_read <= $airfoil_read_stop} {
set_current_airfoil $count_airfoil_read
load_airfoil $current_airfoil
if {$TE_gap_flag == 1} {set_TE_gap $TE_gap $blend_dist}
if {$panel_flag == 1} {panel $n $TE_LE}
# Call oper menu
expect "XFOIL c>" {send "oper\r"}
iter_set $iter set_vpar
142

################# Start of Re number loop ################# # loop variables:
set count_Re 0
while {$count_Re < [llength $Re]} { visc_Re $Re $count_Re $Re_name pacc_on $current_airfoil $current_Re_name
################# Start of AOA loop ################# # loop variables:
set current_AOA $AOA_min
set converged_AOA -1
set converged_failed -1
while {$current_AOA <= $AOA_max & $converged_failed == -1} { while {$converged_AOA == -1 & $converged_failed == -1} {
#expect "c>" {send "init\r"}
#expect "assumed*c>" {send "init\r"}\
# "will*next*c>" {send "cpmn\r"}
alfa $current_AOA
set current_AOA [expr $current_AOA + $AOA_step]
if {$current_AOA > [expr $AOA_max + $AOA_step]} {
set converged_failed 1 }
}
if {$converged_AOA == 1} {
set_par BL $AOA_BL $AOA_BL_name if {$par_data == 1} {
expect "c>" {send "dump $output_folder/BL/$current_output_AOA_par_file\r"} }
set_par H $AOA_H $AOA_H_name if {$par_data == 1} {
expect "c>" {send "vplo\r"}
expect "c>" {send "h\r"}
expect "c>" {send "dump $output_folder/H/$current_output_AOA_par_file\r"} expect "c>" {send "\r"}
}
set_par CP $AOA_CP $AOA_CP_name if {$par_data == 1} {
expect "c>" {send "cpwr $output_folder/CP/$current_output_AOA_par_file\r"} 143

} }
if {$converged_failed == 1} {
close
#missing_rec "$current_airfoil\_$current_Re_name\_N$N_crit $failed_reason"
"progress.txt"
spawn "$xfoil_dir./xfoilP4.exe" x_reset
set converged_failed -1
}
set converged_AOA -1 }
################# End of AOA loop ################# set timeout 2
incr count_Re 1
pacc_off
}
################# End of Re number loop ################# incr count_airfoil_read 1
# Return to start up XFOIL C> expect "c>" {send "\r"}
}
################# End of airfoil loop #################

