---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_IS_ATTACKING
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_IS_ATTACKING
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="PLAYER_IS_ATTACKER_REQUIREMENTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLAYER_IS_ATTACKER_REQUIREMENTS",
		"REQUIREMENT_PLAYER_IS_ATTACKING"
	);


```
