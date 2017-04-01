import {Component, OnInit} from '@angular/core';

@Component({
  template: ''
})
export abstract class OAuthAuthorizer extends OnInit {
  abstract getAuthorizationFullUrl(): string;

  ngOnInit(): void {
    window.location.href = this.getAuthorizationFullUrl();
  }
}
