// fuselage.scainclude <../wart-data.scad>
include <../wart_data.scad>
use <./tail_boom.scad>
use <./motor_stick.scad>
use <../propeller/propeller.scad>
use <./fin.scad>

module fuselage() {
  // position motor stick
  motor_stick();

  // slide tail boom into position
  translate([
    ms_length - tb_overlap,
    spar_size/2,
    tail_boom_elevation
  ])
    tail_boom();
    translate([ms_length + tail_boom_length - 2-spar_size,0,tail_boom_elevation])
    fin();
  rotate([-30,0,0])
  propeller();
}

fuselage();

