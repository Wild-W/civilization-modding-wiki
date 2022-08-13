---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_NUKE_LOVER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_NUKE_LOVER
>
> * Class: `PLAYERS`
> * Arguments:
>	* UsedNukeValue `Integer`
>	* TotalScoreThreshold `Integer`
>	* BuiltNukeValue `Integer`
>	* BelowThreshold `Boolean`

## Samples

```SQL {title="REQUIRES_HIGH_NUKE_LOVE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_HIGH_NUKE_LOVE",
		"REQUIREMENT_PLAYER_NUKE_LOVER"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_HIGH_NUKE_LOVE",
		"BuiltNukeValue",
		1
	),
	(
		"REQUIRES_HIGH_NUKE_LOVE",
		"TotalScoreThreshold",
		0
	),
	(
		"REQUIRES_HIGH_NUKE_LOVE",
		"UsedNukeValue",
		1
	);
	```

```SQL {title="REQUIRES_LOW_NUKE_LOVE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_LOW_NUKE_LOVE",
		"REQUIREMENT_PLAYER_NUKE_LOVER"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_LOW_NUKE_LOVE",
		"BelowThreshold",
		1
	),
	(
		"REQUIRES_LOW_NUKE_LOVE",
		"BuiltNukeValue",
		1
	),
	(
		"REQUIRES_LOW_NUKE_LOVE",
		"TotalScoreThreshold",
		1
	),
	(
		"REQUIRES_LOW_NUKE_LOVE",
		"UsedNukeValue",
		1
	);
	```
