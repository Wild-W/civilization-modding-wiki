---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_ATTACKED_CONTINENT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_ATTACKED_CONTINENT
>
> * Class: `PLAYERS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_ATTACKED_CONTINENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_ATTACKED_CONTINENT",
		"REQUIREMENT_PLAYER_ATTACKED_CONTINENT"
	);

```
