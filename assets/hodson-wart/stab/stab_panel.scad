include <../wart_data.scad>

module stab_panel() {
  le_angle = atan2(0.75,   stab_span/2);
  tip_rib_offset = stab_span/2*tan(le_angle);

  //leading edge
  difference() {
    rotate([0,0,-le_angle])
      translate([0,-0.5,0])
        cube([spar_size, stab_span/2 * 1.1, spar_size]);
    translate([-0.5,-1,-0.5])
      cube([3,1,1]);
    translate([0,stab_span/2,-0.5])
      cube([2,1,1]);
  }

  // trailing edge
  translate([stab_center_chord - spar_size,0,0])
    cube([spar_size, stab_span/2, spar_size]);

  // tip spar
  translate([spar_size+tip_rib_offset, stab_span/2-spar_size,0])
  cube([stab_tip_chord-2 * spar_size,spar_size, spar_size]);
}

stab_panel();
