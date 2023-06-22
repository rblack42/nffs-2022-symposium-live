//##################################################################
// rounded post.scad - square post with rounded top
// (c) 2021 - Roie R. Black
// docs: https://rblack.github.io/math-magik/magik/rounded_post.html

$fn=100;

module rounded_post(z1=3, z2=2.5, t = 0.25, center=true) {
  off = (center)? t/2: 0;
  coff = (center)?0: t/2;
  union() {
    translate([-off,-off,0])
      cube([t,t,z2]);
    translate([coff,coff,z2])
      cylinder(r=t/2, h=z1-z2);
  }
}

rounded_post();

