// elliptic_blade_blank.scad
$fn=64;

module _ellipse(width, height) {
  scale([1, height/width, 1]) circle(r=width/2);
}

module elliptic_blade_blank(
    s=8,
    c=3,
    f=2,
    s1=3,
    s2=5,
    s3=2,
    s4=2) {
  // first quadrant
  translate([0,s-s4])
    intersection() {
      _ellipse(2 * (c-f),2 * s4);
      translate([0,0]) square([(c-f),s4]);
   }
  // second quadrant
  translate([0,s1])
  intersection() {
    _ellipse(2 * f,2 * s2);
    translate([-f,0]) square([f,s2]);
  }
  // third quadrant
  translate([0,s1])
  intersection() {
    _ellipse(2 * f,2 * s1);
    translate([-f,-s1]) square([f,s1]);
  }
  // fourth quadrant
  //translate([0,s3])
  intersection() {
    translate([0,s3])
      _ellipse(2 *(c-f),2 * s3);
    square([(c-f),s3]);
  }
  // trailing edge flat
  translate([0,s3]) square([c-f,s-s3-s4]);
}

elliptic_blade_blank();

