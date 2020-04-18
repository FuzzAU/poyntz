// var app = new Vue({
//     el: '#poyntz',
//     data: {
//       message: 'Hello Vue!'
//     },
//     delimiters: ['[[' , ']]']
//   })

// Vue.component('award-button', {
//   props: ['category', 'point-type'],
//   templates: '<button class="btn">Hello</button>'
// })

$(document).ready(function() {

  $('.award-button').click(function() {
    var category = $(this).data('category');
    var type = $(this).data('type');
    console.log('Awarding ' + type + ' to ' + category);
    
    $.ajax({
      type: "POST",
      url: '/award?category=' + category + '&point_type=' + type
    });
  });

});