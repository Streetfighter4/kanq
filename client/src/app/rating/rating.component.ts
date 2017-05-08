import {Component, EventEmitter, Input, Output} from '@angular/core';
import {Rating} from './rating';

@Component({
  moduleId: module.id,
  selector: 'rating',
  templateUrl: '/rating.component.html',
  styleUrls: ['/rating.component.css']
})
export class RatingComponent{
  @Input() user_rating: Rating;
  @Input() rating: number;
  @Output() onRatingChanged: EventEmitter<any> = new EventEmitter();

  voteClicked(clickedValue: number) {
    this.updateRating(clickedValue);

    // If the user clicked on the upvote button, but the object
    // is already upvoted, remove the upvote instead
    this.user_rating.value = this.user_rating.value == clickedValue ? null : clickedValue;

    let emittedValue = this.user_rating.value || 0;
    this.onRatingChanged.emit(emittedValue);
  }

  private updateRating(clickedValue: number) {
    if(this.user_rating.value) {
      if(this.user_rating.value == clickedValue)
        this.rating -= clickedValue;
      else
        this.rating += clickedValue - this.user_rating.value;
    }
    else
      this.rating += clickedValue;
  }
}
