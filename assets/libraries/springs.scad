use <Naca_Sweep.scad> // for explanation refer to https://www.thingiverse.com/thing:900137


module spring(r=5, R=40, windings=5, H=150, center = true, R1 = undef, start=false, end=false, ends=undef, w = undef, h=undef, reverse=false, pitch = 0)
{
  N = $fn?$fn:180/$fa;
  M_ = ceil(N*windings*R/r); // slices
  h = h?h:2*r;
  R1 = R1?R1:R;
  slope = atan(H/windings/2/R/PI);
  dist = norm([R1-R, H]/windings)/2;
  if(w && abs(R1-R)/windings<=w && abs(H/windings)<=h)
    echo(str("<font color=\"red\">Warning: Self intersection. F6 will have no valid result!</font>"));
  if(!w && dist<=r)
    echo(str("<font color=\"red\">Warning: Self intersection. F6 will have no valid result! r &lt; ", dist, " expected</font>"));
  translate([0, 0, center?-H/2:0])
  {
    tr = spring(r, R, windings, H, R1, w, h, reverse, pitch);
    sweep(tr);
    if (ends||start) sweep(ends(R1,0, w, h), close = true);
    if (ends || end) sweep(ends(R,H, w, h), close = true);
  }

  function ends(R, H, w, h) = let(m = M_/windings)
  let(shape = w&&h?rect(w,h):spring_circle2D(r, N))
  [for (i=[0:m-1]) let(W = -360/m*i)
    T_(0,0,H,
      Rz_(W,
      Tx_(R,
        Rx_(slope-90,
          vec3D(shape)))))];


  function trajectory(R, R1, windings, H, w = undef, h = undef) =  // prepare data for sweep()
  let(f=reverse?-1:1)
  let(shape = w&&h?spring_rect(w,h):spring_circle2D(r, N))
  [for (i=[0:M_]) let(W = 360*windings/M_*i)
    let(R2 = R1+i/M_*(R-R1))
    Rz_(f*W,
      T_(R2, 0, H/M_*i,
        Rx_((slope-90)*f,
          vec3D(shape))))];
}

function spring(r=5, R=40, windings=5, H=150, R1=undef, w = undef, h = undef, reverse=false, pitch = 0) =  // prepare data for sweep()
  let(N = $fn?$fn:180/$fa)
  let(M = ceil(N*windings*R/r)) // slices
  let(f=reverse?-1:1, h = h?h:2*r, R1 = R1?R1:R)
  let(slope = atan(H/windings/2/R/PI))
  let(shape = w&&h?spring_rect(w,h):spring_circle2D(r, N))
  [for (i=[0:M]) let(W = 360*windings/M*i)
    let(R2 = R1+i/M*(R-R1))
    Rz_(f*W,
      T_(R2, 0, H/M*i,
        Rx_((slope-90)*f,
          Rz_(pitch, vec3D(shape)))))];

  function spring_circle2D(r=10, N=40) =  // polygon for cross section
  [for (i=[0:N]) let(w = 360/N*i) r*[sin(w), cos(w)]];

  function spring_rect(a,b) = [[a/2, b/2], [-a/2, b/2],[-a/2, -b/2], [a/2, -b/2]];
