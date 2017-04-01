import {Component, OnInit} from '@angular/core';
import {Settings} from '../settings';

@Component({
  template: ''
})
export abstract class OauthAuthorizer extends OnInit {
  abstract getAuthorizationFullUrl(): string;

  ngOnInit(): void {
    window.location.href = this.getAuthorizationFullUrl();
  }
}
