def project_pipeline(img, src, dst):
	img_unwarp, M, Minv = unwarp(img, src, dst)
	grad_img = pipeline(img_unwarp)
	left_fit, right_fit, left_lane_inds, right_lane_inds = poly_fit(grad_img)
	l_curv, r_curv, dist = curv_and_dist(test_img, left_fit, right_fit, left_lane_inds, right_lane_inds)
	curv = (l_curv + r_curv) / 2
	out_img = fill_lane(img, grad_img, left_fit, right_fit, Minv)
	result = print_data(out_img, curv, dist)
	return result
    