$(function(){

    var Type = Backbone.Model.extend({});
    var Step = Backbone.Model.extend({});
    // -- Views
    var TypeView = Backbone.View.extend({
        tagName: 'li',
        className: 'type-links',
        events:{
            'click a' : 'setactive',
        },
        showsteps: function(){
            var that = this;
            $('#types-steps').slideUp(200,function(){
                var steporder = that.model.get('stepOrder');
                var stepCollection = new StepCollection();
                var stepCollectionView = new StepCollectionView({collection:stepCollection});
                if(steporder.length > 0){
                   $('#types-steps').html(stepCollectionView.el);
                }else{
                    $('#types-steps').html("No Steps listed.");
                }
                for (i=0;i<steporder.length; i++){
                    stepCollection.add(steporder[i]);
                }
                $('#types-steps').delay(200).slideDown(200);
            });
        },
        setactive: function(){
            if($(this.el).hasClass('active')){
            }else{
                $('li.type-links').removeClass('active');
                $(this.el).addClass('active');
                this.showsteps();
            }
        },
        render: function(){

            var html = "<a href='#' class='step-set-link'>"+this.model.get('title')+"</a>";
            $(this.el).html(html);
            return this;
        }
    });
    
    var StepView = Backbone.View.extend({
        render: function(){
            var html = "" +
             "<div class='accordion' id='accordion1'>" +
                "<div class='accordion-group'>" +
                    "<div class='accordion-heading'>" +
                    "<a class='accordion-toggle' data-toggle='collapse' data-parent='#accordion1' href='#collapse"+this.model.get('id')+"'>"+this.model.get('stepNumber') +' - '+ this.model.get('step').title+"</a></div>" +
                    "<div id='collapse"+this.model.get('id')+"' class='accordion-body collapse'>" +
                        "<div class='accordion-inner'>" + this.model.get('step').description + 
                        "</div>"+
                    "</div>"+
                "</div>"+
            "</div>";

            $(this.el).html(html);
            return this;
        }
    });

    // -- Collection
    var TypeCollection = Backbone.Collection.extend({
        url: '/type/?format=json',
        model: Type,
    });

    var StepCollection = Backbone.Collection.extend({
        model: Step,
        comparator: function(step) {
            return step.get("stepNumber");
        },
    });

    // -- Collection View
    var TypeCollectionView = Backbone.View.extend({
        id: 'ul',
        className: 'nav',
        initialize: function(){
            this.collection.on('add', this.addOne, this);
            this.collection.bind('reset' , this.addAll, this);
            this.collection.fetch();
        },
        render: function(){
            this.addAll();
            return this;
        },
        addOne: function(type){
            var typeView = new TypeView({model:type});
            this.$el.append(typeView.render().el);
            this.$el.append("<li class='divider-vertical'></li>");
        },
        addAll: function(){
            this.$el.html('');
            this.collection.forEach(this.addOne, this);
        },
    });

    var StepCollectionView = Backbone.View.extend({
        id: '',
        className: '',
        initialize: function(){
            this.collection.on('add', this.addOne, this);
            this.collection.bind('reset' , this.addAll, this);
        },
        render: function(){
            this.addAll();
            return this;
        },
        addOne: function(step){
            var stepView = new StepView({model:step});
            this.$el.append(stepView.render().el);
        },
        addAll: function(){
            this.$el.html('');
            this.collection.forEach(this.addOne, this);
        },
    });
    
    typeCollection = new TypeCollection();
    typeCollectionView = new TypeCollectionView({collection:typeCollection});
    $('#types-buttons').html(typeCollectionView.el);

});

