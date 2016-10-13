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

  $scope.post = function() {
    $http({
      method: 'post',
      url: '/translate',
      data: {
        csrfmiddlewaretoken: '{{ csrf_token }}',
        text: $scope.text
      }
    }).then(function setTranslation(res) {
      console.log(res)
    }, function errcallback(res){
      console.log(res)
    })
  }
}])
