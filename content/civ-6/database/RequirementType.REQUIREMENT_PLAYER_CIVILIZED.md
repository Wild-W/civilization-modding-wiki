---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_CIVILIZED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_CIVILIZED
>
> * Class: `PLAYERS`
> * Arguments:
>	* TotalScoreThreshold `Integer`
>	* IgnoredCampValue `Integer`
>	* ClearedCampValue `Integer`
>	* CampToCityDistance `Integer`
>	* BelowThreshold `Boolean`

## Samples

```SQL {title="REQUIRES_CLEARS_BARBARIAN_CAMPS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CLEARS_BARBARIAN_CAMPS",
		"REQUIREMENT_PLAYER_CIVILIZED"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CLEARS_BARBARIAN_CAMPS",
		"CampToCityDistance",
		10
	),
	(
		"REQUIRES_CLEARS_BARBARIAN_CAMPS",
		"ClearedCampValue",
		1
	),
	(
		"REQUIRES_CLEARS_BARBARIAN_CAMPS",
		"IgnoredCampValue",
		1
	),
	(
		"REQUIRES_CLEARS_BARBARIAN_CAMPS",
		"TotalScoreThreshold",
		0
	);
	```

```SQL {title="REQUIRES_IGNORES_BARBARIAN_CAMPS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_IGNORES_BARBARIAN_CAMPS",
		"REQUIREMENT_PLAYER_CIVILIZED"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_IGNORES_BARBARIAN_CAMPS",
		"BelowThreshold",
		1
	),
	(
		"REQUIRES_IGNORES_BARBARIAN_CAMPS",
		"CampToCityDistance",
		10
	),
	(
		"REQUIRES_IGNORES_BARBARIAN_CAMPS",
		"ClearedCampValue",
		1
	),
	(
		"REQUIRES_IGNORES_BARBARIAN_CAMPS",
		"IgnoredCampValue",
		1
	),
	(
		"REQUIRES_IGNORES_BARBARIAN_CAMPS",
		"TotalScoreThreshold",
		1
	);
	```
