//######################################
// prop_bearing_2D.scad
// (c) Roie R. Black
//**************************************
use <MMlib/circular_arc_strip.scad>
$fn=100;

module prop_bearing_2D(
  length = 0.4,         // prop to rear
  height = 0.15,         // top to prop-shaft
  front_height = 3/64,  // nose height
  top_length = 0.2,     // top flat length
  thickness = 1/64      // material thickness
) {
  bend_radius = 2 * thickness;

  // geometry calculations
  d = height - bend_radius;
  ky = d - front_height;
  kx = length - 2 * bend_radius - top_length;
  b = sqrt(kx*kx + ky*ky);
  alpha = atan2(kx,ky);
  echo(b,d,kx,ky,alpha,thickness);

  // locate bend centers
  p1 = [2 * thickness, front_height];
  p2 = p1 + [kx,ky];
  p3 = [length - 2 * thickness,d];

  // front flat
  square([thickness,front_height]);

  // first bend at p1
  translate(p1) circular_arc_strip(bend_radius,180-alpha,180,thickness);

  // sloped front flat
  translate(p1 + [-bend_radius * cos(alpha), bend_radius*sin(alpha)])
    rotate(-alpha)
      square([thickness, b]);

  // second bend at p2
  translate(p2) circular_arc_strip(bend_radius, 90,180-alpha,thickness);

  // top flat
  translate([p2.x,p2.y + thickness]) square([top_length,thickness]);

  // third bend at p3
  translate(p3) circular_arc_strip(bend_radius, 0,90,thickness);
  // segment 5 - top
  // back flat
  translate([length - thickness,0])
    square([thickness,d]);
}

//---------------------------------------
// debug display

prop_bearing_2D();
