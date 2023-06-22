//#######################################################################
// single_taper_spar.scad - spat tapered on one side
// (c) 2021 - Roie R. Black
// docs: https://rblack.github.io/math-magik/magik/single_taper_spar.html

module single_taper_spar(l=5, z1=1, z2=0.5, t=1, debug=false) {
  // calculate taper angle
  ang = atan2(z1-z2,l);

  difference() {
    // basic spar
    cube([l,t,z1]);

    // trimming block
    translate([0,-t/2, z1])
    rotate([0,ang,0])
    if (debug) {
      #cube([l+1, 2*t, z1]);
    } else {
      cube([l+1, 2*t, z1]);
    }
  }
}

single_taper_spar(debug=true);
