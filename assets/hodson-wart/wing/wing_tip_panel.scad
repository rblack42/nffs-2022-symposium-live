include <../wart_data.scad>

module wing_tip_panel() {
  le_angle = atan2(
    wing_center_chord - wing_tip_chord,           wing_center_span/2 + wing_tip_span);
    wing_center_tip_rib_offset = 
        wing_center_span/2*tan(le_angle);
    ting_tip_rib_offset = wing_center_chord -           wing_tip_chord;
    
        echo(wing_center_tip_chord);
    echo(wing_center_tip_rib_offset);
  //leading edge
  difference() {
    rotate([0,0,-le_angle])
      translate([0,-0.5,0])
        cube([spar_size, wing_tip_span * 1.2, spar_size]);
    translate([-0.5,-1,-0.5])
      cube([3,1,1]);
    translate([0,wing_tip_span,-0.5])
      cube([2,1,1]);
  }

  // trailing edge
  translate([wing_center_chord - spar_size,0,0])
    cube([spar_size, wing_tip_span, spar_size]);

  // tip spar
  translate([
    spar_size+wing_tip_rib_offset, 
    wing_tip_span/-spar_size,
    0
  ])
  cube([wing_tip_chord- wing_tip_rib_offset -2 * spar_size,spar_size, spar_size]);
  
}

wing_tip_panel();
