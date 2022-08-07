---
tags:
- EffectType
title: EFFECT_DIPLOMACY_AGENDA_KUBLAI_PAX
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_DIPLOMACY_AGENDA_KUBLAI_PAX
>
> * Class: `Unknown`
> * Parameters:
>	* StatementKey `Unknown`

## Samples

```SQL {title="AGENDA_KUBLAI_PAX"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		OwnerRequirementSetId,
		SubjectRequirementSetId
	)
VALUES
	(
		"AGENDA_KUBLAI_PAX",
		"MODIFIER_PLAYER_DIPLOMACY_AGENDA_KUBLAI_PAX",
		"ON_TURN_STARTED",
		"PLAYER_IS_MAJOR_CIV_KNOWN_30_TURNS"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"AGENDA_KUBLAI_PAX",
		"StatementKey",
		"AGENDA_KUBLAI_PAX_KUDO_AND_WARNING"
	);
	
```

