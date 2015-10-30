hidden_opt = [[32,32],[32,16,8],[100]]
l1_opt = [1e-5,1e-7]

hyper_parameters = {"hidden":hidden_opt, "l1":l1_opt}

from h2o.grid.grid_search import H2OGridSearch

model_grid = H2OGridSearch(H2ODeepLearningEstimator, hyper_params=hyper_parameters)
model_grid.train(x=x, y=y, distribution="multinomial", training_frame=train, validation_frame=test)
