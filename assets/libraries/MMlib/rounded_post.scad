//########################################################
// rounded post.scad - square post with rounded top
// (c) 2021 - Roie R. Black
//========================================================
$fn=100;

module rounded_post(z1=3, z2=2.5, t = 0.25) {
  union() {
      translate([-t/2,-t/2,0])
      cube([t,t,z2]);
      translate([0,0,z2])
      cylinder(r=t/2, h=z1-z2);
  }
}

rounded_post();

