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
    this.onRatingChanged.emit(this.user_rating.value);
  }

  private updateRating(clickedValue: number) {
    // TODO: Technically it's working, but it should probably be refactored... a lot
    if(this.user_rating.value != null) {
      if(this.user_rating.value == 1) {
        if(clickedValue == 1) {
          this.rating += -1;
        }
        if(clickedValue == -1) {
          this.rating += -2;
        }
      }
      if(this.user_rating.value == -1) {
        if(clickedValue == 1) {
          this.rating += 2;
        }
        if(clickedValue == -1) {
          this.rating += 1;
        }
      }
    }
    if(this.user_rating.value == null) {
      this.rating += clickedValue;
    }
  }
}
