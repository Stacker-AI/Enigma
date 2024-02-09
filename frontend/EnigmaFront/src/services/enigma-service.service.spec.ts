import { TestBed } from '@angular/core/testing';

import { EnigmaServiceService } from './enigma-service.service';

describe('EnigmaServiceService', () => {
  let service: EnigmaServiceService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(EnigmaServiceService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
