const React = require('react');
const ReactDOM = require('react-dom');

class QuestionsList extends React.Component {
    constructor(props) {
        super(props);
        this.state = {url : props.url, pollInterval: props.pollInterval};
    }

    loadQuestionsFromServer() {
        $.ajax({
            url: this.setState({url: this.state.url + 'questions/?format=json'}),
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState({data: data});
            }.bind(this),
            error: function(err) {
                console.log(err);
            }
        });
    }

    getInitialState() {
        return {data: ['No questions']};
    }

    componentDidMount() {
        this.loadQuestionsFromServer();
        setInterval(this.loadQuestionsFromServer,
            this.state.pollInterval)
    }

    render() {
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
}


ReactDOM.render(<QuestionsList url='/api/' pollInterval={1000} />, document.getElementById('container'));