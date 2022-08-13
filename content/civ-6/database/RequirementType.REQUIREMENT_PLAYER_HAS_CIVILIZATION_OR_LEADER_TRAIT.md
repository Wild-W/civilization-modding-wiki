---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_CIVILIZATION_OR_LEADER_TRAIT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_CIVILIZATION_OR_LEADER_TRAIT
>
> * Class: `PLAYERS`
> * Arguments:
>	* TraitType `String`

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_NOBEL_PRIZE_TRAIT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_NOBEL_PRIZE_TRAIT",
		"REQUIREMENT_PLAYER_HAS_CIVILIZATION_OR_LEADER_TRAIT"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_NOBEL_PRIZE_TRAIT",
		"TraitType",
		"TRAIT_CIVILIZATION_NOBEL_PRIZE"
	);
	
```
