App = Ember.Application.create();

App.Store = DS.Store.extend({
    revision: 12,
    adapter: 'DS.FixtureAdapter'
});

App.Router.map(function() {
    this.resource('torrents', function(){
        this.resource('torrent', { path: ':torrent_id' })
    });
});

App.TorrentsRoute = Ember.Route.extend({
    model: function() {
        return App.Torrent.find();
    }
});

App.AddTorrentView = Ember.View.create({

    torrentUrl: "wallop",
    classNames: ['navbar-form', 'pull-right'],

    submitTorrent: function(e) {
        console.log(this.get('torrentUrl'));
        console.log(arguments);
    }
});

App.Torrent = DS.Model.extend({
    name: DS.attr('string'),
});

App.Torrent.FIXTURES = [{
    id: 1,
    name: 'my torrent'
}, {
    id: 2,
    name: 'my torrent 2'
}]
