---
tags:
- RequirementType
title: REQUIREMENT_OPEN_BORDERS
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_OPEN_BORDERS
>
> * Class: `PLAYERS`
> * Arguments:
>	* GracePeriod `Integer`

## Samples

```SQL {title="REQUIRES_PLAYER_OPEN_BORDERS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_OPEN_BORDERS",
		"REQUIREMENT_OPEN_BORDERS"
	);

```

```SQL {title="REQUIRES_PLAYER_NO_OPEN_BORDERS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLAYER_NO_OPEN_BORDERS",
		"REQUIREMENT_OPEN_BORDERS",
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
		"REQUIRES_PLAYER_NO_OPEN_BORDERS",
		"GracePeriod",
		2
	);
	```
