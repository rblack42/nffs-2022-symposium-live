//####################################
// rib.scad - circular arc rib
// (c) 2021 by Roie R. Black
//====================================
use <MMlib/trimming_rib_strip.scad>

module circular_arc_rib(ch,ca,h,t,ale,ate) {

  // calculate the radius for this arc
  ca = ch * ca / 100;
  rad = (ch * ch) / (8 * ca) + ca/2;
  theta = 90 - 2 * atan2(ch - 2*ca,ch + 2*ca);
  echo(rad,theta);
  rc = rad * sin(theta);
  echo(rc);

  // generate the rib
  difference() {
    translate([-0.2,0,0])
      rotate([90,0,0])
        translate([0,0,-t/2])
          linear_extrude(height=t)
            trimming_rib_strip(rad,ch,h);

    // trim front for le spar
    translate([-ch/2,0,0])
    rotate([0,0,ale])
    translate([-0.5,0,0])
       color("red")
         cube([1,2,1],center=true);

    // trim rear for te spar
    translate([ch/2,0,0])
      rotate([0,0,ate])
        translate([0.5,0,0])
        color("red")
          cube([1,2,1],center=true);
  }
}

//====================================
// display this shape

circular_arc_rib(5,4,1/16,1/32,60,-30);


