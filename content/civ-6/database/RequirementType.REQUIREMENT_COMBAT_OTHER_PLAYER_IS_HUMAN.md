---
tags:
- RequirementType
title: REQUIREMENT_COMBAT_OTHER_PLAYER_IS_HUMAN
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COMBAT_OTHER_PLAYER_IS_HUMAN
>
> * Class: `Unknown`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRE_OTHER_COMBAT_PLAYER_IS_AI"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRE_OTHER_COMBAT_PLAYER_IS_AI",
		"REQUIREMENT_COMBAT_OTHER_PLAYER_IS_HUMAN",
		1
	);


```