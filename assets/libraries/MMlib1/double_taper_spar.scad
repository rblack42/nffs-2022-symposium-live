//######################################################################
// double_taper_spar.scad - creates a spar tapered on two sides
// (c) 2021 - Roie R. Black
// docs: https://rblack.github.io/math-magik/magik/double_taper_spar.html

module double_taper_spar(l=5, y1=1, y2=0.5, z1=1, z2=0.5, debug=false) {
  // calc taper angles
  yang = atan2(z1-z2,l);
  zang = atan2(y1-y2,l);


  difference() {
    // z taper
    difference() {
      cube([l,y1,z1]);
      translate([0,-y1/2, z1])
        rotate([0,yang,0])
          if (debug) {
            #cube([l+1, 2*y1, z1]);
          } else {
            cube([l+1, 2*y1, z1]);
          }
    // y taper
    translate([0,y1, -z1/2])
      rotate([0,0,-zang])
        if (debug) {
          #cube([l+1, y1, 2*z1]);
        } else {
          cube([l+1, y1, 2*z1]);
        }
    }
  }
}

double_taper_spar();
