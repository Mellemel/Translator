var myApp = angular.module('MyApp', [])

myApp.controller('TabCtrl', ['$scope', function($scope) {
    $scope.tab = 1;

    $scope.setTab = function(newTab){
      $scope.tab = newTab;
    };

    $scope.isSet = function(tabNum){
      return $scope.tab === tabNum;
    };
}])

myApp.controller('TextCtrl', ['$scope', '$http', function($scope, $http) {
  $http.defaults.xsrfCookieName = 'csrftoken';
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';

  $scope.text = ''
  $scope.translations = []

  // make http request to get list for returning users
  $http.get('/retrieve').then(function(res){
    console.log(res)
    $scope.translations = res.data.data
  })

  //post 
  $scope.post = function() {
    $http({
      method: 'post',
      url: '/translate',
      data: {
        csrfmiddlewaretoken: '{{ csrf_token }}',
        text: $scope.text
      }
    }).then(function(res) {
      $scope.translations.push(res.data)
    }, function(res){
      console.log(res)
    })
    $scope.text = ''
  }
  $scope.remove = function (id) {
    console.log(id)
  }
}])
