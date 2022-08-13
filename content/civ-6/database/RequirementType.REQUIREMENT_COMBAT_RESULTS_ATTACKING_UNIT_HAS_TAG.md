---
tags:
- RequirementType
title: REQUIREMENT_COMBAT_RESULTS_ATTACKING_UNIT_HAS_TAG
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COMBAT_RESULTS_ATTACKING_UNIT_HAS_TAG
>
> * Class: `Unknown`
> * Arguments:
>	* Tag `Unknown`

## Samples

```SQL {title="REQUIREMENT_ZOMBIE_TAG_ATTACKER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_ZOMBIE_TAG_ATTACKER",
		"REQUIREMENT_COMBAT_RESULTS_ATTACKING_UNIT_HAS_TAG"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIREMENT_ZOMBIE_TAG_ATTACKER",
		"Tag",
		"CLASS_ZOMBIE"
	);
	```
