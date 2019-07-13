
var calendar = new FullCalendar.Calendar(document.getElementById('calendar'), {
  events: 'events.json',
  plugins: [ 'bootstrap', 'dayGrid', 'timeGrid' ],
  themeSystem: 'bootstrap',
  defaultView: 'dayGridMonth',
  header: {
    left: 'dayGridMonth,timeGridWeek,timeGridDay',
    center: 'title',
    right: 'today prevYear,prev,next,nextYear'
  },
  eventRender: function(info) {
    tippy(info.el, {
      content: info.event.title,
      animation: 'scale',
      interactive: true
    });
  }
});

calendar.render();
