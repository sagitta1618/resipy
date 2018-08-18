#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 16:46:04 2018

@author: jkl
"""

r2help = {
  'flux_type': "<p>Define the flux type to be used (either 2D or 3D)</p>",
  'res_matrix' : "<p><code>res_matrix</code> is 1 if a 'sensitivity' matrix is required for the converged solution. This matrix is not the Jacobian but is the diagonal of [J^T.W^T.W.J] which gives an idea of the mesh sensitivity (see equation 5.20 of Binley and Kemna, 2005)</p><p>Set <code>res_matrix</code> to 2 if the true resolution matrix is computed for a converged solution and the diagonal is stored (see equation 5.18 of Binley and Kemna,  2005), note that this calculation is more time consuming than the ‘sensitivity matrix’ option.</p><p>Set <code>res_matrix</code> to 3 if the sensitivity map is required and an out put of the jacobian matrix and roughness matrix.</p><p>If neither sensitivity map or resolution matrix is required then set <code>res_matrix</code> to 0.</p>",
  'singular_type' : "<p>Note that singularity removal can only be applied is (a) the boundaries are infinite and (b) the y=0 plane defines the upper boundary. </p>",
  'inverse_type' : "<p>where <code>inverse_type</code> is 0 for pseudo-Marquardt solution or 1 for regularised solution with linear filter (usual mode) or 2 for regularised type with quadratic filter or 3 for qualitative solution or 4 for blocked linear regularised type. Note that the blocking defined here is only for a quadrilateral mesh – for blocking within a triangular mesh see the details for preparing <code>mesh.dat</code></p>",
  'target_decrease': "<p><code>target_decrease</code> is a real number which allows the user to specify the relative reduction of misfit in each iteration. A value of 0.25 will mean that R2 will aim to drop the misfit by 25% (and no more) of the value at the start of the iteration. This allows a slower progression of the inversion, which can often result in a better convergence. If you set <code>target_decrease</code> to 0.0 then R2 will try to achieve the maximum reduction in misfit in the iteration.</p> ",
  'qual_code' : "<p>where <code>qual_ratio</code> is 0 for qualitative comparison with forward solution, i.e. only when one observed data set is available, or <code>qual_ratio</code> is 1 if the observed data in protocol.dat contains a ratio of two datasets.</p>",
  'rho_max' : "<p>where <code>rho_min</code> and <code>rho_max</code> are the minimum and maximum observed apparent resistivity to be used.</p>",
  'scale' : "<p>where <code>scale</code> is a scaling factor for the mesh coordinates. This is usually 1.0 but if astandardised mesh is used, say for a unit circle, then this scaling factor is useful to adjust themesh for a specific problem. Set <code>scale</code>=1 if you do not wish to change the coordinates of themesh defined in <code>mesh.dat</code></p>",
  'num_regions' : "<p>where <code>num_regions</code> is number of resistivity regions that will be specified either as starting condition for inverse solution or actual model for forward solution. The term “region” has no significance inthe inversion – it is just a means of inputting a non-uniform resistivity as a starting model for inversion or for forward calculation.</p>",
  'patch' : "<p>where <code>patch_size_x</code> and <code>patch_size_y</code> are the parameter block sizes in the x and y direction, respectively. Note that the number of elements in the x direction must be perfectly divisible by <code>patch_size_x</code> and the number of elements in the y direction must be perfectly divisible by <code>patch_size_y</code> otherwise set them both to zero. </p>",
  'data_type' : "<p>where <code>data_type</code> is 0 for true data based inversion or 1 for log data based. Note that the latter should improve convergence but may not work for internal electrodes (e.g. borehole type) where the polarity can change due to resistivity distributions</p>",
  'reg_mode' : "<p><code>reg_mode</code> is 0 for normal regularisation; or 1 if you want to include regularisation relative to your starting resistivity (this is whatever you have set in input lines 11 to 13); or 2 if you wish to regularise relative to a previous dataset using the “Difference inversion” of LaBrecque and Yang (2000). If you select <code>reg_mode</code>=1 then Line 22 will require a regularisation parameter alpha_s. If you select <code>reg_mode</code>=2 then protocol.dat must contain an extra column (see below) with the reference dataset. In addition, your starting model (see Line 12) should be the inverse model for this reference dataset (i.e. you need to invert the reference dataset before running the time-lapse inversion). Also note that if you select <code>reg_mode</code>=2 then <code>data_type</code> is automatically set to 0 irrespective of what was entered in Line 21.</p>",
  'tolerance' : "<p>where <code>tolerance</code> is desired misfit (usually 1.0)</p>",
  'max_iterations' : "<p><code>max_iterations</code> is the maximum number of iterations.</p>",
  'error_mod' : "<p><code>error_mod</code> is 0 if you wish to preserve the data weights, 1 or 2 if you wish the inversion to update the weights as the inversion progresses based on how good a fit each data point makes. <code>error_mod</code>=2 is recommended – this is a routine based on Morelli and LaBrecque (1996). Note that no weights will be increased.</p>",
  'alpha_aniso' : "<p>The smoothing factor used in the code (alpha) is searched for at each iteration. The search is done over a range of steps in alpha, the number of steps is <code>num_alpha_steps</code>. <code>alpha_aniso</code> is the anisotropy of the smoothing factor, set <code>alpha_aniso</code> > 1 for smoother horizontal models, <code>alpha_aniso</code> < 1 for smoother vertical models, or <code>alpha_aniso</code>=1 for normal (isotropic) regularisation.</p>",
  'alpha_s' : "<p><code>alpha_s</code> is the regularisation to the starting model (if you set <code>reg_mode</code> = 1 in Line 21). Set <code>alpha_s</code> to a high value (e.g. 10) to highly penalise any departure from this starting model. Note that <code>alpha_s</code> will stay fixed – if you set it too high then R2 may not converge. R2.out will report the value of alpha used to regularise smoothing within the image – the regularisation relative to a reference model is additional to this. The user may find setting <code>alpha_s</code> useful as a comparison of inversions from two runs with difference reference models allows an assessment of the depth of investigation following the approach of Oldenburg and Li (1999).</p>",
  'errorParam' : "<p>It is advisable to estimate <code>a_wgt</code> and <code>b_wgt</code> from error checks in the field data (ideally from reciprocal measurements - not measures of repeatability). Typically for surface data <code>a_wgt</code> will be about 0.01 ohms and <code>b_wgt</code> will be about 0.02 (roughly equivalent to 2% error). Note that if you select data_type=1 in Line 21 then although the resistance data are transformed into log apparent conductivities the <code>a_wgt</code> and <code>b_wgt</code> parameters should still reflect the variance of the resistance; <code>rho_min</code> and <code>rho_max</code> are the minimum and maximum observed apparent resistivity to be used for inversion (use large extremes if you want all data to be used). If data are ignored by R2 because of the apparent resistivity limits then these will be reported individually in R2.log. NOTE: that the apparent resistivity calculations assume that you have set the ground surface to Y=0 and that the ground surface is flat. Note also that you can select to include individual errors for each measurement in the data input file protocol.dat – to do this <code>a_wgt</code> and <code>b_wgt</code> should be set to 0.0 – protocol.dat will then require an additional column (see later).</p>",
  'num_xy_poly' : "<p>where <code>num_xy_poly</code> is the number of x,y co-ordinates that define a polyline bounding the output volume. If <code>num_xy_poly</code> is set to zero then no bounding is done in the x-y plane. The co-ordinates of the bounding polyline follow in the next line. NOTE: the first and last pair of co-ordinates must be identical (to complete the polyline). So, for example, if you define a bounding square in x,y then you must have 5 co-ordinates on the polyline. The polyline must be defined as a series of co-ordinates in sequence, although the order can be clockwise or anti-clockwise (see examples later). NOTE: R2 stores the vertical co-ordinates for nodes in a quadrilateral mesh with a convention positive upwards. For example, if the ground surface has an elevation of 0m and you wish to output to a depth of 8m then y=-8m must be used for the lower boundary of the polygon. Similarly, if the ground surface elevation is 100m and you wish to output to a depth of 8m then y=-92m must be used for the lower boundary of the polygon. This was not the convention for v2.7a and so any input files created for that version must be changed (this only applies to line 26). If a triangular mesh is used then the co-ordinates specified in the mesh file are used and the above comments about sign convention do not apply. </p>"
  }

