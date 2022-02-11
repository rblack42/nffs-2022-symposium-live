include <./wart_data.scad>
use <fuselage/fuselage.scad>
use <stab/stab.scad>
include <MMlib/colors.scad>

module wart() {
	fuselage();
  translate([
    ms_length+tail_boom_length-tb_overlap-stab_center_chord,
    0,
    tail_boom_elevation])
      color(WOOD_Balsa)
        stab();
}

wart();

