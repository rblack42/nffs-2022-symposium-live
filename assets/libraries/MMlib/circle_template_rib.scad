//####################################
// rib.scad - circle template rib
// (c) 2021 by Roie R. Black
//====================================
$fn=360;
module circle_template_rib(chord,camber,height,thickness) {

  // calculate the radius for this arc
  camber = chord * camber / 100;
  radius = (chord * chord) / (8 * camber) + camber/2;
  // generate the rib
  translate([0,thickness/2,0])
    rotate([90,0,0])
      linear_extrude(height = thickness) {
        intersection() {
          difference() {
            square([chord,1]);
            translate([chord/2, -radius + camber]) circle(r=radius);
          }
          translate([chord/2, -radius + camber + height]) circle(r=radius);
        }
      }
}
//====================================
// display this shape

circle_template_rib(5,4,1/16,1/32);


