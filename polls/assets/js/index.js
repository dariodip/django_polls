const React = require('react');
const ReactDOM = require('react-dom');

class QuestionsList extends React.Component {

    constructor(props) {
        super(props);
        this.state = {url : props.url + 'questions/?format=json',
            pollInterval: props.pollInterval,
            data: []};
        this.loadQuestionsFromServer = this.loadQuestionsFromServer.bind(this);
    }

    loadQuestionsFromServer() {
        $.ajax({
            url: this.state.url,
            datatype: 'json',
            cache: false,
            success: function(data) {
                this.setState((prevState, props) => {
                    return {data: data}}
                );
            }.bind(this),
            error: function(err) {
                console.log(err);
            }
        });
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
                return(
                    <li className="collection-item" key={question.id}>
                        <i className="material-icons">label</i>
                        {question.question_text}
                    </li>)
            });
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