const React = require('react');
const ReactDOM = require('react-dom');

var QuestionsList = React.createClass({

    loadQuestionsFromServer: function(){
        $.ajax({
            url: this.props.url + 'questions/?format=json',
            datatype: 'json',
            cache: false,
            success: function(data) {
                console.log(data);
                this.setState({data: data});
            }.bind(this),
            error: function(err) {
                console.log(err);
            }
        })
    },

    getInitialState: function() {
        return {data: ['No questions']};
    },

    componentDidMount: function() {
        this.loadQuestionsFromServer();
        setInterval(this.loadQuestionsFromServer,
            this.props.pollInterval)
    },
    render: function() {
        var totalQuestions = 0;
        if (this.state.data) {
            totalQuestions = this.state.data.length;
            var questionNodes = this.state.data.map(function(question){
                return <li className="collection-item" key={question.id}> {question.question_text} </li>
            })
        }
        return (
            <div>
                <ul className="collection with-header">
                    <li className="collection-header"><h5>Found {totalQuestions} questions</h5></li>
                    {questionNodes}
                </ul>
            </div>
        )
    }
});

ReactDOM.render(<QuestionsList url='/api/' pollInterval={1000} />, document.getElementById('container'));