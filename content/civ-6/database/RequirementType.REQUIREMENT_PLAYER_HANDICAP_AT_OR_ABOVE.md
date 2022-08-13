---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HANDICAP_AT_OR_ABOVE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HANDICAP_AT_OR_ABOVE
>
> * Class: `PLAYERS`
> * Arguments:
>	* Handicap `String`

## Samples

```SQL {title="REQUIRES_EMPEROR_OR_HIGHER_DIFFICULTY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_EMPEROR_OR_HIGHER_DIFFICULTY",
		"REQUIREMENT_PLAYER_HANDICAP_AT_OR_ABOVE"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_EMPEROR_OR_HIGHER_DIFFICULTY",
		"Handicap",
		"DIFFICULTY_EMPEROR"
	);
	```
