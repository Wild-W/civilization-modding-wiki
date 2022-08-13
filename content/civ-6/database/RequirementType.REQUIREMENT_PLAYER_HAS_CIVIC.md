---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_CIVIC
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_CIVIC
>
> * Class: `PLAYERS`
> * Arguments:
>	* CivicType `String`
>		* [Civics.CivicType]

## Samples

```SQL {title="REQUIRES_PLAYER_DOES_NOT_HAVE_NATURAL_HISTORY"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLAYER_DOES_NOT_HAVE_NATURAL_HISTORY",
		"REQUIREMENT_PLAYER_HAS_CIVIC",
		1
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_DOES_NOT_HAVE_NATURAL_HISTORY",
		"CivicType",
		"CIVIC_NATURAL_HISTORY"
	);
	```
