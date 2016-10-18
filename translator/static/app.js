var myApp = angular.module('MyApp', ['ui.router'])

myApp.config(function ($stateProvider) {
  $stateProvider
    .state({
      name: 'translator',
      url: '',
      templateUrl: '/static/views/translator.html',
      controller: function ($scope, translationFactory) {
        $scope.text = ''
        $scope.submitForm = function () {
          translationFactory.translateText($scope.text)
        }
      }
    })
    .state({
      name: 'list',
      url: 'list',
      templateUrl: '/static/views/list.html',
      resolve: {
        translations: function (translationFactory) {
          return translationFactory.getAllTranslations()
        }
      },
      controller: function ($scope, translations) {
        $scope.translations = translations.data
      }
    })
})

myApp.factory('translationFactory', function ($http, $q) {
  $http.defaults.xsrfCookieName = 'csrftoken';
  $http.defaults.xsrfHeaderName = 'X-CSRFToken';

  var service = {}

  service.translateText = function (text) {
    $http.post('/translate', { text: text })
  }

  service.getAllTranslations = function () {
    var deferred = $q.defer()
    $http.get('/retrieve')
      .then(function (res) {
        deferred.resolve(res.data)
      }, function (errr) {
        console.error(error)
      })
      return deferred.promise
  }
  return service
})